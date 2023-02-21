package main

import (
	"context"
	"encoding/json"
	"flag"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"strings"

	gogpt "github.com/sashabaranov/go-gpt3"
)

var (
	dir      = flag.String("dir", "", "Path to the files to summarize")
	apiToken = flag.String("api-token", "", "OpenAI API token")
)

func main() {
	ctx := context.Background()
	// Disable timestamp in STDERR log
	log.SetFlags(0)

	flag.Parse()
	if *dir == "" {
		log.Fatalf("Please specify a directory with files to summarize via `--dir` CLI argument.\n")
	} else if *apiToken == "" {
		log.Fatalf("Please specify an API token via `--api-token` CLI argument.\nYou can get one at https://platform.openai.com/account/api-keys.\n")
	}

	linksContent, err := os.ReadFile(*dir + "/../links.html")
	if err != nil {
		log.Fatalln("Couldn't read links file:", err)
	}
	linksString := string(linksContent)

	c := gogpt.NewClient(*apiToken)

	promptPrefix := "The following text is the transcript of a talk given at the FOSDEM conference in 2023. FOSDEM is about free and open source software development. Because the transcript was created by a speech-to-text machine learning model, there might be some errors and typos. There might also be a Questions and Answers section at the end. Please summarize the talk in a few sentences, while leaving out the Q&A section."

	entries, err := os.ReadDir(*dir)
	if err != nil {
		log.Fatalln("Couldn't read directory:", err)
	}
	for _, entry := range entries {
		if entry.IsDir() || filepath.Ext(entry.Name()) != ".json" {
			continue
		}

		filePath := filepath.Join(*dir, entry.Name())
		jsonString, err := os.ReadFile(filePath)
		if err != nil {
			log.Println("Couldn't read file:", err)
			continue
		}
		transcript := struct {
			Text string `json:"text"`
		}{}
		err = json.Unmarshal(jsonString, &transcript)
		if err != nil {
			log.Println("Couldn't unmarshal JSON:", err)
			continue
		}

		// OpenAPI GPT-3's Davinci 003 model only allows 4000 tokens, which is around 3000 words.
		// Splitting in chunks will make the model lose context, so we skip long transcripts.
		// With the prompt prefix and summary completion, let's check for 2700 words.
		if len(strings.Fields(transcript.Text)) > 2700 {
			log.Println("File too long, skipping.", entry.Name(), "has", len(strings.Fields(transcript.Text)), "words.")
			continue
		}

		fmt.Println("Summarizing", entry.Name())

		req := gogpt.CompletionRequest{
			Model:     gogpt.GPT3TextDavinci003,
			MaxTokens: 256,
			Prompt:    promptPrefix + "\n\n" + transcript.Text,
		}
		resp, err := c.CreateCompletion(ctx, req)
		if err != nil {
			log.Println("Couldn't create GPT-3 completion:", err)
			continue
		}

		summaryFilePath := strings.TrimSuffix(filePath, ".json") + ".summary.txt"
		err = os.WriteFile(summaryFilePath, []byte(resp.Choices[0].Text), 0644)
		if err != nil {
			log.Println("Couldn't write summary file:", err)
			continue
		}

		// Link in HTML
		// Replace `<a href="files/foo.webm.json">JSON</a>`
		// with `<a href="files/foo.webm.summary.txt">Summary</a> <a href="files/foo.webm.json">JSON</a>`
		old := `<a href="files/` + entry.Name() + `">JSON</a>`
		new := `<a href="files/` + strings.TrimSuffix(entry.Name(), ".json") + ".summary.txt" + `">Summary</a> ` + old
		linksString = strings.Replace(linksString, old, new, -1)
	}

	err = os.WriteFile(*dir+"/../links.html", []byte(linksString), 0644)
	if err != nil {
		log.Fatalln("Couldn't write links file:", err)
	}
}
