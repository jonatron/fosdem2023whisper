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

	"github.com/pkoukk/tiktoken-go"
	"github.com/sashabaranov/go-openai"
)

// Flags
var (
	dir       = flag.String("dir", "", "Path to the files to summarize")
	apiToken  = flag.String("api-token", "", "OpenAI API token")
	dry       = flag.Bool("dry", false, "Dry run (don't actually summarize)")
	overwrite = flag.Bool("overwrite", false, "Overwrite existing summaries")
)

func main() {
	ctx := context.Background()
	// Disable timestamp in STDERR log
	log.SetFlags(0)

	flag.Parse()
	if *dir == "" {
		log.Fatalf("Please specify a directory with files to summarize via `--dir` CLI argument.\n")
	} else if *apiToken == "" && !*dry {
		log.Fatalf("Please specify an API token via `--api-token` CLI argument.\nYou can get one at https://platform.openai.com/account/api-keys.\n")
	}

	// Tokenizer for dry run / estimating cost, but also choosing model to save on cost.
	tt, err := tiktoken.EncodingForModel(openai.GPT3Dot5Turbo)
	if err != nil {
		log.Fatalln("Couldn't get tokenizer:", err)
	}

	// OpenAI client
	c := openai.NewClient(*apiToken)

	promptPrefix := "The following text is the transcript of a talk given at the FOSDEM conference in 2023. FOSDEM is about free and open source software development. Because the transcript was created by a speech-to-text machine learning model, there might be some errors and typos. There might also be a Questions and Answers section at the end. Please summarize the talk in a few sentences, while leaving out the Q&A section."

	entries, err := os.ReadDir(*dir)
	if err != nil {
		log.Fatalln("Couldn't read directory:", err)
	}
	var priceEstimateSum float64
	for _, entry := range entries {
		if entry.IsDir() || filepath.Ext(entry.Name()) != ".json" {
			continue
		}
		talkName := strings.TrimSuffix(entry.Name(), ".webm.json")

		// If overwrite option is false, entry if summary already exists.
		if !*overwrite {
			summaryFilePath := filepath.Join(*dir, talkName+".webm.summary.txt")
			if _, err := os.Stat(summaryFilePath); err == nil {
				log.Println("Summary for", talkName, "already exists, skipping.")
				continue
			}
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

		fmt.Println("Summarizing", talkName)

		req := openai.ChatCompletionRequest{
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: promptPrefix + "\n\n" + transcript.Text,
				},
			},
		}

		// Calculate token count, both for dry run / estimating cost, but also choosing model to save on cost
		inputTokensCount := len(tt.Encode(req.Messages[0].Role, nil, nil))
		inputTokensCount += len(tt.Encode(req.Messages[0].Content, nil, nil))
		// Plus summary output, which is roughly 100 words, which is roughly +33% in tokens.
		outputTokenCount := 133

		var priceEstimate float64
		// For pricing check https://openai.com/pricing, section "Chat".
		if inputTokensCount+outputTokenCount > 16000 {
			log.Println("File too long (exceeding 16k tokens), skipping.")
			continue
		} else if inputTokensCount+outputTokenCount > 4000 {
			req.Model = openai.GPT3Dot5Turbo16K
			priceEstimate = 0.003 / 1000 * float64(inputTokensCount)
			priceEstimate += 0.004 / 1000 * float64(outputTokenCount)
		} else {
			req.Model = openai.GPT3Dot5Turbo
			priceEstimate = 0.0015 / 1000 * float64(inputTokensCount)
			priceEstimate += 0.002 / 1000 * float64(outputTokenCount)
		}
		priceEstimateSum += priceEstimate

		if *dry {
			log.Printf("%v tokens; estimated cost: $%.2f\n", inputTokensCount+outputTokenCount, priceEstimate)
			continue
		}

		resp, err := c.CreateChatCompletion(ctx, req)
		if err != nil {
			log.Printf("Couldn't create completion with %v: %v\n", req.Model, err)
			continue
		}
		summary := resp.Choices[0].Message.Content
		summary = strings.TrimSpace(summary)
		if summary == "" {
			log.Println("Empty summary, skipping.")
			continue
		}

		summaryFilePath := strings.TrimSuffix(filePath, ".json") + ".summary.txt"
		err = os.WriteFile(summaryFilePath, []byte(summary), 0644)
		if err != nil {
			log.Println("Couldn't write summary file:", err)
			continue
		}

		err = writeLink(*dir, entry.Name())
		if err != nil {
			log.Fatalf("Couldn't write link: %v\n", err)
		}
	}

	log.Printf("Estimated total cost: $%.2f\n", priceEstimateSum)
}

func writeLink(dir, fileName string) error {
	// Link in HTML
	// Replace `<a href="files/foo.webm.json">JSON</a>`
	// with `<a href="files/foo.webm.summary.txt">Summary</a> <a href="files/foo.webm.json">JSON</a>`
	// But only if the summary link doesn't exist yet (to allow re-running this CLI multiple times).
	linksContent, err := os.ReadFile(dir + "/../links.html")
	if err != nil {
		return fmt.Errorf("couldn't read links file: %w", err)
	}
	linksString := string(linksContent)
	summaryLink := `<a href="files/` + strings.TrimSuffix(fileName, ".json") + ".summary.txt" + `">Summary</a>`
	if !strings.Contains(linksString, summaryLink) {
		old := `<a href="files/` + fileName + `">JSON</a>`
		new := summaryLink + " " + old
		linksString = strings.Replace(linksString, old, new, -1)
	}
	err = os.WriteFile(dir+"/../links.html", []byte(linksString), 0644)
	if err != nil {
		return fmt.Errorf("couldn't write links file: %w", err)
	}

	return nil
}
