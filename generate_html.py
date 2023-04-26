import json
import os

'''
let links = document.querySelectorAll('#main td a')
let linklist = [];
for(let link of links) {
    if(link.href.includes("webm")) {
        let title = link.closest('tr').querySelector('td').innerText;
        linklist.push({'href': link.href, 'title': title})
    }
}
'''


files = [
  {
    "href": "https://video.fosdem.org/2023/Janson/celebrating_25_years_of_open_source.webm",
    "title": "Celebrating 25 years of Open Source\nPast, Present, and Future"
  },
  {
    "href": "https://video.fosdem.org/2023/Janson/nasa.webm",
    "title": "Open Source Software at NASA"
  },
  {
    "href": "https://video.fosdem.org/2023/Janson/closing_fosdem.webm",
    "title": "Closing FOSDEM 2023"
  },
  {
    "href": "https://video.fosdem.org/2023/Janson/cyber_resilience.webm",
    "title": "How regulating software for the European market could impact FOSS"
  },
  {
    "href": "https://video.fosdem.org/2023/Janson/elisa.webm",
    "title": "The ELISA Project - Enabling Linux in Safety Applications\nProjects insights and overview"
  },
  {
    "href": "https://video.fosdem.org/2023/Janson/linux_inlaws.webm",
    "title": "Linux Inlaws\nA how-to on world domination by accident"
  },
  {
    "href": "https://video.fosdem.org/2023/Janson/similarity_detection.webm",
    "title": "Similarity Detection in Online Integrity\nFighting abusive content with algorithms"
  },
  {
    "href": "https://video.fosdem.org/2023/Janson/firefox_testing.webm",
    "title": "Teaching machines to handle bugs and test Firefox more efficiently.\nUsing machine learning to automate bug management, test selection, and more."
  },
  {
    "href": "https://video.fosdem.org/2023/Janson/sustaining_foss.webm",
    "title": "Sustaining Free and Open Source Software\nExploring Community, Financial, and Engineering Practices"
  },
  {
    "href": "https://video.fosdem.org/2023/Janson/developer_experience.webm",
    "title": "Perspectives from the Open Source Developer\nA Window into the Developer Experience from Linux Foundation Research"
  },
  {
    "href": "https://video.fosdem.org/2023/Janson/sustainability.webm",
    "title": "Open Source in Environmental Sustainability\nPreserving climate and natural resources with openness"
  },
  {
    "href": "https://video.fosdem.org/2023/Janson/open_source_communities.webm",
    "title": "Making the world a better place through Open Source\nFocusing the unique power of Open Source Communities as force of social good in today's complex geopolitical landscape"
  },
  {
    "href": "https://video.fosdem.org/2023/Janson/software_supply_chain.webm",
    "title": "Building Strong Foundations for a More Secure Future\nAddressing The Systemic Issues in the Software Supply Chain that Led to Log4Shell"
  },
  {
    "href": "https://video.fosdem.org/2023/Janson/rosegarden.webm",
    "title": "Rosegarden: A Slumbering Giant\nHow a 20-year old OSS project is still going strong"
  },
  {
    "href": "https://video.fosdem.org/2023/Janson/podcasting20.webm",
    "title": "Podcasting 2.0: it's all about Interoperability\nHow Podcasting 2.0 will save the Open Internet"
  },
  {
    "href": "https://video.fosdem.org/2023/Janson/hachyderm.webm",
    "title": "Decentralized Social Media with Hachyderm\nGrowing into medium scale, incident report, and forming Nivenly"
  },
  {
    "href": "https://video.fosdem.org/2023/Janson/plumbers.webm",
    "title": "Running a Hybrid Event with Open Source\nThe Plumbers Experience"
  },
  {
    "href": "https://video.fosdem.org/2023/Janson/matrix20.webm",
    "title": "Matrix 2.0\nHow we’re making Matrix go voom"
  },
  {
    "href": "https://video.fosdem.org/2023/K.1.105%20(La%20Fontaine)/graphics_a_frames_journey.webm",
    "title": "Graphics: A Frame's Journey"
  },
  {
    "href": "https://video.fosdem.org/2023/K.1.105%20(La%20Fontaine)/open_source_chip_design.webm",
    "title": "Can we do an open source chip design in 45 minutes?\nThe state of free and open source silicon"
  },
  {
    "href": "https://video.fosdem.org/2023/K.1.105%20(La%20Fontaine)/fedora_asahi.webm",
    "title": "Fedora Asahi\nFedora for Apple SIlicon"
  },
  {
    "href": "https://video.fosdem.org/2023/K.1.105%20(La%20Fontaine)/dnf5.webm",
    "title": "DNF5: the new era in RPM software management\nHow we rewrote the codebase and started loving the community"
  },
  {
    "href": "https://video.fosdem.org/2023/K.1.105%20(La%20Fontaine)/browser_maker_tools.webm",
    "title": "Maker Tools in the Browser\nCAM to 3D Printing: Zero Install, Always Up to Date"
  },
  {
    "href": "https://video.fosdem.org/2023/K.1.105%20(La%20Fontaine)/passwordless.webm",
    "title": "Passwordless Linux -- where are we?"
  },
  {
    "href": "https://video.fosdem.org/2023/K.1.105%20(La%20Fontaine)/foss_winners_losers.webm",
    "title": "Winners and Losers in FOSS\nOpen Source Has \"Won\" - Have We?"
  },
  {
    "href": "https://video.fosdem.org/2023/K.1.105%20(La%20Fontaine)/fair_threaded_task_scheduler.webm",
    "title": "Fair threaded task scheduler verified in TLA+"
  },
  {
    "href": "https://video.fosdem.org/2023/K.1.105%20(La%20Fontaine)/wikidata_openstreetmap.webm",
    "title": "Tools for linking Wikidata and OpenStreetMap\nSoftware for adding links between open data projects"
  },
  {
    "href": "https://video.fosdem.org/2023/K.1.105%20(La%20Fontaine)/rust_coreutils.webm",
    "title": "Reimplementing the Coreutils in a modern language (Rust)\nDoing old things with modern tools"
  },
  {
    "href": "https://video.fosdem.org/2023/K.1.105%20(La%20Fontaine)/zero_knowledge_crypto.webm",
    "title": "Zero Knowledge Cryptography and Anonymous Engineering\nThe development of zk-snarks in recent years and explosion in algos has opened up an entire new design space of anonymous engineering."
  },
  {
    "href": "https://video.fosdem.org/2023/K.1.105%20(La%20Fontaine)/plant_monitoring.webm",
    "title": "Building an Plant Monitoring App with InfluxDB, Python, and Flask with Edge to cloud replication\nPlant monitoring with open source tools"
  },
  {
    "href": "https://video.fosdem.org/2023/K.1.105%20(La%20Fontaine)/home_automation.webm",
    "title": "Practical Computerized Home Automation"
  },
  {
    "href": "https://video.fosdem.org/2023/K.1.105%20(La%20Fontaine)/business_guidebook.webm",
    "title": "The Open Source Business Guidebook\nBuilding a Scalable OSS Based Business"
  },
  {
    "href": "https://video.fosdem.org/2023/K.1.105%20(La%20Fontaine)/open_source_startup.webm",
    "title": "Starting an Open Source Startup\nWhat you need to know before starting your own open source startup"
  },
  {
    "href": "https://video.fosdem.org/2023/K.1.105%20(La%20Fontaine)/small_business_using_open_source.webm",
    "title": "Clear skies, no clouds in sight. Running a 14 person company on only free software.\nThey say it can't be done, they say it's too much work. But is it really? After 5 years of running Prehensile Tales on entirely free software I think I can answer this."
  },
  {
    "href": "https://video.fosdem.org/2023/K.1.105%20(La%20Fontaine)/cloud_threats.webm",
    "title": "The End of Free Software\nHow the Cloud threatens FOSS and what we can do about it"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/helios.webm",
    "title": "Introducing Helios\nA small, practical microkernel"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/pathways_that_invest_in_new_maintainers.webm",
    "title": "Creating Pathways That Invest in New Maintainers"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/standards_in_libre_localization.webm",
    "title": "Should there be a standard in libre localization?\nIdeas on how to make it easy for translators to contribute to any FOSS project they like"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/awkward_user_interviews.webm",
    "title": "Do more awkward user interviews\nDo you feel awkward interviewing users about how they use your project? That's ok — awkward interviews are often good interviews."
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/beyond_wikipedia.webm",
    "title": "Beyond Wikipedia: Discovering Wikimedia's Open-Source Ecosystem"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/data_mountains.webm",
    "title": "data mountains - turn your data into mountains!\nconvert geospatial points into triangles scaled by data"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/coffeosm.webm",
    "title": "CoffeOSM: improve OpenStreetMap a receipt at a time\nchecking and add shop on the map with a receipt"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/pg_statviz.webm",
    "title": "Announcing pg_statviz"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/breaking_code_of_inclusion.webm",
    "title": "Breaking the Code of Inclusion: Designing Micro Materials Based on PRIMM Principles for Accessible Programming Education."
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/open_source_good_governance.webm",
    "title": "Open Source Good Governance – GGI Framework presentation & deployment\nA quick introduction to the OSPO Alliance handbook and resources"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/fpga_music_synthesis.webm",
    "title": "FPGA-based music synthesis with open-source tools"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/fabaccess.webm",
    "title": "FabAccess\na machine access system for fablabs and makerspaces"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/openstreetmap_emergency_eyes.webm",
    "title": "OpenStreetMap: Sharpen your \"Emergency Eyes\"\nDisaster prep mapping in the EU"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/bare_metal_servers_as_container_runtime.webm",
    "title": "Bare-metal servers as a container runtime"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/passbolt.webm",
    "title": "Passbolt\nOpen source password manager for teams"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/is_yaml_the_answer.webm",
    "title": "Is YAML the Answer?\n… and if so, what has ever been the question?"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/cni_2_0.webm",
    "title": "CNI 2.0: Vive la révolution"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/staging_of_artifacts_in_build_system.webm",
    "title": "Staging of Artifacts in a Build System"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/jitsi_appointment_management.webm",
    "title": "Combining EASY!Appointments with Jitsi for online appointment management"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/breaking_from_big_tech.webm",
    "title": "Breaking away from Big Tech\nUsing open source infrastructure in a convenient way"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/grottocenter.webm",
    "title": "Grottocenter\nAn open source database for cavers"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/consulting_for_digital_humanists.webm",
    "title": "Consulting for digital humanists\nthe cultural shock developing tools and pedagogy"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/gitlab_forge_for_teachers_and_students_in_france.webm",
    "title": "A GitLab forge for all teachers and students in France?\nA project of the French Ministry of Education"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/fossbot.webm",
    "title": "FOSSbot: An open source and open design educational robot"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/tableaunoir.webm",
    "title": "Tableaunoir: an online blackboard for teaching"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/lua_for_the_lazy_c_developer.webm",
    "title": "Lua for the lazy C developer"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/i2p_major_changes.webm",
    "title": "I2P: Major Changes of the Peer-to-Peer Network\nCryptography of I2P Received a Major Update - an Overview of the Changes and its Impacts"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/nym_mixnet.webm",
    "title": "The Nym Mixnet\nIntro to a new anonymous communication network"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/keyoxide.webm",
    "title": "Keyoxide: verifying online identity with cryptography\nA novel approach to secure decentralized online identity"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/gallia.webm",
    "title": "gallia: An Extendable Pentesting Framework"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/jubako.webm",
    "title": "Jubako, a new generic container format\nA new file format to store contents all together"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/self_hosting_for_non_coders.webm",
    "title": "Self-hosting for non-coders?\nThe open-source approach"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/libre_soc.webm",
    "title": "Libre-SOC: From architecture and simulation to test silicon, and beyond\nA design for a fully documented and transparent hybrid CPU-GPU-VPU core, for a family of System-on-Chip products"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/open_source_formal_verification.webm",
    "title": "Get Started with Open Source Formal Verification"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/ngi_search_and_openwebsearch.webm",
    "title": "NGI Search and OpenWebSearch.EU projects\nTwo sister initiatives for a paradigm change in open search and discovery on the internet"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2215%20(Ferrer)/fosdem_infrastructure.webm",
    "title": "FOSDEM infrastructure review"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/bintools_fq.webm",
    "title": "fq - jq for binary formats"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/bintools_kaitai.webm",
    "title": "Parsing binary formats with Kaitai Struct"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/bintools_poke.webm",
    "title": "GNU poke\nThe extensible editor for structured binary data"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/bintools_stackunwind.webm",
    "title": "Stack walking/unwinding without frame pointers"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/bintools_libabigail.webm",
    "title": "Libabigail, State Of The Onion\nCurrent status and perspectives of the Libabigail project"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/bintools_poked.webm",
    "title": "GNU poke beyond the CLI (Command Line Interface)\npoked + pokelets = Better UI"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/bintools_radare2.webm",
    "title": "The state of r2land\nPresenting radare2, last updates and development plans"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/welcome_to_the_bsd_devroom_2023.webm",
    "title": "Welcome to the BSD devroom"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/bsd_driver_harmony.webm",
    "title": "BSD Driver Harmony\nImproving collaboration between the major BSDs on driver development"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/game_of_trees_daemon.webm",
    "title": "Game of Trees Daemon\nA Git repository server for OpenBSD and other systems"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/reggae_jails_vms_on_freebsd.webm",
    "title": "Reggae: cool way of managing jails/VMs on FreeBSD\nNo docker, no cry"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/happy_5th_anniversary_pkg_provides.webm",
    "title": "Happy 5th anniversary pkg-provides"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/chimera_linux.webm",
    "title": "Chimera Linux\nA BSD/LLVM distro from scratch"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/collab_collabora_online.webm",
    "title": "Collaborating with Collabora Online\nHow to re-use Collabora in your work or project"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/collab_xwiki.webm",
    "title": "Migrating from proprietary to Open-Source knowledge management tools"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/collab_fess.webm",
    "title": "Deploy an enterprise search server with Fess\nSearch GitLab, Redmine, and repositories with a single query"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/collab_openproject.webm",
    "title": "Optimizing your core application for integration\nLearnings from integrating OpenProject with Nextcloud"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/collab_nextcloud.webm",
    "title": "Nextcloud Numbers and Hubs\nOur traditional yearly overview of what's new in Nextcloud"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/collab_tiki.webm",
    "title": "The Relentless March of Markdown\nAnd its arrival in Tiki 25"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/collab_cryptpad.webm",
    "title": "Privacy and Collaboration\nHow CryptPad lets you have both"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/collab_zulip.webm",
    "title": "Transparent, asynchronous, efficient communication\nHow the Zulip open-source team chat application addresses the needs of open-source and research communities"
  },
  {
    "href": "https://video.fosdem.org/2023/D.collab/collab_grav.webm",
    "title": "Conquering tribal knowledge with Grav\nFour years and a pandemic later, where has our Grav setup taken us?"
  },
  {
    "href": "https://video.fosdem.org/2023/D.collab/collab_antora.webm",
    "title": "Creating a content pipeline with Antora\nUsing AsciiDoc content for the website and other downstream processes"
  },
  {
    "href": "https://video.fosdem.org/2023/D.collab/collab_tribe.webm",
    "title": "Tribe - a content structuring and collaborative framework\nJSON compatible and opinionated content-first framework"
  },
  {
    "href": "https://video.fosdem.org/2023/D.collab/collab_alfresco.webm",
    "title": "Open Source Collaboration Tools for Alfresco\nEnhancing Collaboration Experience with CSP"
  },
  {
    "href": "https://video.fosdem.org/2023/D.collab/collab_onlyoffice.webm",
    "title": "Tackling document collaboration challenges in 2023"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/welcome_community.webm",
    "title": "Welcome to the Community Devroom"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/building_external_evangelists.webm",
    "title": "Building External Evangelists\nWhat should be the primary goal of every community team"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/learned_leading_healthy_project.webm",
    "title": "What I learned about leading a healthy project from speaking to 50+ maintainers"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/cultural_relativism.webm",
    "title": "Cultural Relativism\na Prism for Constructing Cross Cultural Communities"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/contributor_experience.webm",
    "title": "Contributor Experience 201\nSupporting social infrastructure in FOSS projects"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/free_culture_cv_show_community_contributions.webm",
    "title": "Free Culture CV\nan open source idea to show the community your contributions"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/uncover_missing_link.webm",
    "title": "Uncover the Missing Link\nCreating Clear Linkage between Open Source and Standards"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/community_interactive.webm",
    "title": "Just A Community Minute"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/nurture_motivate_recognise_noncode_contributions.webm",
    "title": "Nurturing, Motivating and Recognizing Non-Code Contributions"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/public_money_public_code.webm",
    "title": "If it’s public money, make it public code!\nHow to effectively push for Free Software all over Europe"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/contributor_growth_strategies_oss_project.webm",
    "title": "Contributor Growth Strategies for OSS Projects"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/centering_dei_within_os_project.webm",
    "title": "Centering DEI Within Your Open Source Project"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/building_open_souce_teams.webm",
    "title": "Building Open Source Teams"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/do_we_need_virtual_events.webm",
    "title": "Do we still need to have virtual events?\nMy learnings from organizing virtual community events"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/community_closed.webm",
    "title": "Community Closing remarks"
  },
  {
    "href": "https://video.fosdem.org/2023/D.confidential/cc_online_rust.webm",
    "title": "Rust based Shim-Firmware for confidential container"
  },
  {
    "href": "https://video.fosdem.org/2023/D.confidential/cc_online_veraison.webm",
    "title": "Project Veraison (VERificAtIon of atteStatiON)\n(Trying to) making sense of chaos"
  },
  {
    "href": "https://video.fosdem.org/2023/D.confidential/cc_online_nydus.webm",
    "title": "Nydus Image Service for Confidential Containers"
  },
  {
    "href": "https://video.fosdem.org/2023/D.confidential/cc_online_base.webm",
    "title": "THE BASE - FOSS Confidential Container SDK to ease the development"
  },
  {
    "href": "https://video.fosdem.org/2023/D.confidential/cc_online_vulnerabilities.webm",
    "title": "A Study of Fine-Grain Compartment Interface Vulnerabilities: What, Why, and What We Should Do About Them"
  },
  {
    "href": "https://video.fosdem.org/2023/D.confidential/cc_online_enarx.webm",
    "title": "Building a secure network of trusted applications on untrusted hosts"
  },
  {
    "href": "https://video.fosdem.org/2023/D.confidential/cc_online_marblerun.webm",
    "title": "Scalable Confidential Computing on Kubernetes with Marblerun"
  },
  {
    "href": "https://video.fosdem.org/2023/D.confidential/cc_online_gramine.webm",
    "title": "Gramine Library OS\nRunning unmodified Linux applications in Intel SGX enclaves"
  },
  {
    "href": "https://video.fosdem.org/2023/D.confidential/cc_online_attestation.webm",
    "title": "Confidential Containers and the Pitfalls of Runtime Attestation"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/cc_movement.webm",
    "title": "We need a Let’s Encrypt movement for Confidential Computing\nThe importance of protecting data in use"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/cc_lskv.webm",
    "title": "LSKV: Democratising Confidential Computing from the Core"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/cc_mrtee.webm",
    "title": "Keeping safety-critical programs alive when Linux isn’t able to\nUsing OP-TEE to deliver availability to applications in a Trusted Execution Environment."
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/cc_riscv.webm",
    "title": "Open Source Confidential Computing with RISC-V"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/cc_ibmz.webm",
    "title": "Introduction to Secure Execution for s390x\nKVM confidential VMs on IBM Z"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/cc_cloud.webm",
    "title": "Tilting a Pyramid\nConfidentiality in a Cloud Native Environment"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/cc_aws.webm",
    "title": "Salmiac: Running unmodified container images in Nitro Enclaves"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/cc_kubernetes.webm",
    "title": "Autonomous Confidential Kubernetes\nHow to securely manage K8s from within K8s"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/cc_closing.webm",
    "title": "Devroom closing and goodbye"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/container_kubernetes_cluster_right_way.webm",
    "title": "Drawing your Kubernetes cluster the right way\nhow to present the cluster without scaring people"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/container_send_in_chown.webm",
    "title": "Send in the chown()s\nsystemd containers in user namespaces"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/container_fedora_coreos.webm",
    "title": "Fedora CoreOS - Your Next Multiplayer Homelab Distro\nUsing Fedora CoreOS in a Selfhosted Homelab to setup a Multiplayer Server"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/container_kubernetes_multi_cloud.webm",
    "title": "Deploying Kubernetes across Hybrid and Multi-Cloud Environments Using OpenNebula"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/container_developer_tooling.webm",
    "title": "Touring the container developer tooling landscape"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/container_reproducible_dockerfile.webm",
    "title": "Bit-for-bit reproducible builds with Dockerfile\nDeterministic timestamps and deterministic apt-get"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/container_kubernetes_criu.webm",
    "title": "Kubernetes and Checkpoint/Restore"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/container_database_containers.webm",
    "title": "Exploring Database Containers"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/container_syscall_interception.webm",
    "title": "Safer containers through system call interception\n(Ab)using seccomp to emulate the world"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/container_bottlerocket_os.webm",
    "title": "Bottlerocket OS - a container-optimized Linux"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/container_kubernetes_secret_rotation.webm",
    "title": "Automating secret rotation in Kubernetes\nMinimizing mistakes by removing the human element"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/container_secure_storage.webm",
    "title": "Quick starting secure container storage using squashfs, overlay and dm-verity"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/container_kubernetes_cluster_api.webm",
    "title": "Cluster API: Operating Kubernetes with Kubernetes"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/container_cgroup_v2.webm",
    "title": "7 years of cgroup v2: the future of Linux resource control"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/container_kubernetes_database_dbaas.webm",
    "title": "From a database in container to DBaaS on Kubernetes"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/container_kubernetes_operators_wasm.webm",
    "title": "Lightweight Kubernetes Operators with WebAssembly\nTowards serverless Kubernetes controllers"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/making_continuous_delivery_accessible_to_all.webm",
    "title": "Making Continuous Delivery Accessible to All"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/how_to_automate_documentation_workflow_for_developers.webm",
    "title": "How To Automate Documentation Workflow For Developers"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/delivering_a_crossplane_based_latform.webm",
    "title": "Delivering a crossplane-based platform"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/continuous_update_everything.webm",
    "title": "Continuously Update Everything\nA recipe for disaster?"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/continuous_delivery_to_many_kubernetes_clusters.webm",
    "title": "Continuous Delivery to many Kubernetes Clusters"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/cicd_formachine_learning_models.webm",
    "title": "CI/CD for Machine learning models\nHow to test ML models?"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/build_cicd_pipelines_as_code_run_them_anywhere.webm",
    "title": "Build CI/CD pipelines as code, run them anywhere"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/how_we_gained_observability_into_our_cicd_pipeline.webm",
    "title": "How We Gained Observability Into Our CI/CD Pipeline\nUsing best of breed open source to monitor Jenkins"
  },
  {
    "href": "https://video.fosdem.org/2023/D.minimalistic/fim.webm",
    "title": "Inside the FIM (Fbi IMproved) Scriptable Image Viewer\nAbout a Small Command Language Powering an Image Viewer"
  },
  {
    "href": "https://video.fosdem.org/2023/D.minimalistic/lipsscheme.webm",
    "title": "LIPS Scheme\nPowerful introspection and extensibility"
  },
  {
    "href": "https://video.fosdem.org/2023/D.minimalistic/prescheme.webm",
    "title": "Introduction to Pre-Scheme"
  },
  {
    "href": "https://video.fosdem.org/2023/D.minimalistic/guixriscv.webm",
    "title": "Bringing RISC-V to Guix's bootstrap\nWhat's done and what we need to do"
  },
  {
    "href": "https://video.fosdem.org/2023/D.minimalistic/guixfhs.webm",
    "title": "Using GNU Guix Containers with FHS (Filesystem Hierarchy Standard) Support"
  },
  {
    "href": "https://video.fosdem.org/2023/D.minimalistic/reflexiveinterpreters.webm",
    "title": "Self-conscious Reflexive Interpreters"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/guixopenscience.webm",
    "title": "GNU Guix and Open science, a crush?"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/replicantguix.webm",
    "title": "How Replicant, a 100% free software Android distribution, uses (or doesn't use) Guix"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/webassemblyforth.webm",
    "title": "Exploring WebAssembly with Forth (and vice versa)\nArtisanal, minimal, just-in-time compilation for the web and beyond"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/whippet.webm",
    "title": "Whippet: A new production embeddable garbage collector\nReplacing Guile's engine while the car is running"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/zigandguile.webm",
    "title": "Zig and Guile for fast code and a REPL"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/fuzionlang.webm",
    "title": "Algebraic Effects and Types as First-Class Features in the Fuzion Language\nGiving a pure functional solution for non-functional aspects."
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/idpz3.webm",
    "title": "IDP-Z3, a reasoning engine for FO(.)\nA truly declarative approach to programming."
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/luarocks.webm",
    "title": "LuaRocks and the challenges of minimalism"
  },
  {
    "href": "https://video.fosdem.org/2023/D.minimalistic/reversepolishlisp.webm",
    "title": "Reviving Reverse Polish Lisp\nBuilding an open-source HP48-like calculator"
  },
  {
    "href": "https://video.fosdem.org/2023/D.minimalistic/guixhome.webm",
    "title": "An Introduction to Guix Home\nDeclarative $HOME configuration with Scheme!"
  },
  {
    "href": "https://video.fosdem.org/2023/D.minimalistic/liberatestorytelling.webm",
    "title": "Literate Storytelling: Interpreting Syntaxes for Explorers\nDemonstration of the use of syntaxes to facilitate the search of information"
  },
  {
    "href": "https://video.fosdem.org/2023/D.minimalistic/tissue.webm",
    "title": "tissue—the minimalist git+plain text issue tracker"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.114%20(Baudoux)/containerised_apps.webm",
    "title": "(Keynote) What could go wrong? Me, I was\nContainerised Applications are the way"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.114%20(Baudoux)/rolling_release_spack.webm",
    "title": "Automating a rolling binary release for Spack\nScaling a modern CI workflow to a large distribution"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.114%20(Baudoux)/automation_debian.webm",
    "title": "Automation for Debian Packaging"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.114%20(Baudoux)/open_mainframe_project.webm",
    "title": "Upstream Collaboration and Linux Distributions Collaboration - Is that excluded?\nThe Linux Distributions Working Group @ The Open Mainframe Project"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.114%20(Baudoux)/linux_gaming_fedora.webm",
    "title": "AMENDMENT Linux Distributions’ State of Gaming\nA Case Study of Fedora Workstation"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.114%20(Baudoux)/anaconda_web_ui.webm",
    "title": "Building a Web UI for the Fedora installer\nthe reasons, the tools and progress so far"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.114%20(Baudoux)/kairos.webm",
    "title": "How we build and maintain Kairos\nA day in the life of a meta distribution"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.114%20(Baudoux)/centos_stream.webm",
    "title": "CentOS Stream\nRHEL development in public"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.114%20(Baudoux)/package_bpf_linux.webm",
    "title": "How to package BPF software for Linux distributions\n…presented on Gentoo Linux"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.114%20(Baudoux)/women_in_linux_foss.webm",
    "title": "From Linux to Cloud to Edge and beyond: Evolution of women contributors in distros & FOSS\nA timeline from past, present, and future"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.114%20(Baudoux)/fixing_2038.webm",
    "title": "Fixing Year 2038\nCoordinating the 64-bit time_t ABI migration"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.114%20(Baudoux)/debug_packages.webm",
    "title": "Creating and distributing debug packages"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.114%20(Baudoux)/kdlp_kernel_devel_learning_pipeline.webm",
    "title": "KDLP: Kernel Development Learning Pipeline\nA comprehensive pipeline for bringing new talent into the the Linux kernel and its orbit"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.114%20(Baudoux)/kubeos.webm",
    "title": "AMENDMENT KubeOS: Container OS based on OpenEuler\nA container operating system based on openEuler and a solution of cluster nodes upgrade"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/dns_parsing_zone_files_really_fast.webm",
    "title": "AMENDMENT Parsing zone files really fast"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/dns_i2p.webm",
    "title": "DNS for I2P: a Distributed Network without Central Authority\nHow Students Tried to Create a DNS for an Overlay Network without a Central Authority"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/dns_why_resolving_two_names_in_a_gui_program_is_hard.webm",
    "title": "Why resolving two names in a GUI program is hard\nSummary of available name resolution APIs on Linux and why a new one is needed"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/dns_connectbyname_and_the_proxy_control_option.webm",
    "title": "Connectbyname and the Proxy Control option"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/dns_iothnamed.webm",
    "title": "iothnamed\na DNS server/forwarder/cache for the Internet of Threads"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/dns_implementation_of_the_drink_server.webm",
    "title": "Implementation of the Drink server: programming details"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/dns_hosting_your_own_dns_for_fun_and_zero_profit.webm",
    "title": "Hosting your own DNS for 'fun' and zero profit"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/dns_moving_from_home_grown_to_open_source.webm",
    "title": "Moving from home grown to open source\nA thrilling tale of RFC non-compliance, wildcard hell and scaling issues"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/dns_bizarre_and_unusual_uses_of_dns.webm",
    "title": "Bizarre and Unusual Uses of DNS\nRule 53: If you can think of it, someone's done it in the DNS"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/delta_like_ota_streaming.webm",
    "title": "Delta-like Streaming of (encrypted) OTA Updates for RAUC"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/matter_and_thread.webm",
    "title": "Matter and Thread as Connectivity Solution for Embedded"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/bt_mesh_rust.webm",
    "title": "Developing Bluetooth Mesh networks with Rust"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/5_errors_when_building.webm",
    "title": "5 errors when building embedded systems"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/wam_runtime.webm",
    "title": "WAM: an embedded web runtime history for LG webOS and Automotive Grade Linux\nIntroduction and retrospective"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/kuksa.webm",
    "title": "KUKSA.val Vehicle Abstraction\nIn-vehicle access to standardized VSS Vehicle Signals"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/linux_camera_apps.webm",
    "title": "Convergent camera applications for mobile Linux devices\nWhat does it take to run your desktop camera application on your phone"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/allwinner_camera.webm",
    "title": "Advanced Camera Support on Allwinner SoCs with Mainline Linux"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/uboot_psci.webm",
    "title": "U-Boot as PSCI provider on ARM64"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/barebox.webm",
    "title": "barebox, the bootloader for Linux kernel developers"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/fpga_bitstreams.webm",
    "title": "Building FPGA Bitstreams with Open-Source Tools"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/open_switching.webm",
    "title": "Open Source Switching: Upstreaming ONIE NVMEM and switch BSP drivers\nAn overview of a DENT upstream WG project and network switch board support in the Linux kernel"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/hw_journey.webm",
    "title": "A journey to the hardware world\nA software engineer retrospective"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/rdp_wayland.webm",
    "title": "Ups and Downs with Remote Desktop Protocol (RDP) on Wayland, Weston and the Yocto Project"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/bt_pipewire.webm",
    "title": "Bluetooth state in PipeWire and WirePlumber"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/ikea_smarthome_hub.webm",
    "title": "Exploring a swedish smarthome hub"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/polyvent.webm",
    "title": "The PolyVent FLOSS Ventilator\nA Free-libre Respiration Ecosystem"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/solar_roof_datalogger.webm",
    "title": "Reverse engineering a solar roof datalogger\n\"Hey, is that a Raspberry Pi in there?\""
  },
  {
    "href": "https://video.fosdem.org/2023/D.emulator/learn_8bit.webm",
    "title": "Learn 8-bit machine language with the Toy CPU emulator\nAn emulator in the style of the Altair 8880 or IMSAI 8080"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/seven_sins.webm",
    "title": "7 things I learned about old computers, via emulation\n(p.s. it's not about games)"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/psp.webm",
    "title": "Pushing the PSP\nEmulating Dreamcast and DS on PSP"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/xilinx.webm",
    "title": "An introduction into AMD/Xilinx libsystemctlm-soc"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/oak.webm",
    "title": "Emulator development in Java"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/csd.webm",
    "title": "OpenCSD, simple and intuitive computational storage emulation with QEMU and eBPF\nAfter all, why not turn your computer into a distributed system?"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/gamma.webm",
    "title": "Understanding the Bull GAMMA 3 first generation computer through emulation"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/gb_arm.webm",
    "title": "I made a GameBoy emulator to learn about computers. And now I work with them...\nA brief personal journey in emulator development (with a sprinkle of Rust and WebAssembly)"
  },
  {
    "href": "https://video.fosdem.org/2023/D.energy/energy_welcome_devroom.webm",
    "title": "Welcome to the online Energy Devroom"
  },
  {
    "href": "https://video.fosdem.org/2023/D.energy/energy_eu_policy.webm",
    "title": "Energy policy by the European Commission\nBrief overview of policies and opportunities for collaboration"
  },
  {
    "href": "https://video.fosdem.org/2023/D.energy/energy_learn_from_other_traditional_industries.webm",
    "title": "What the energy industry can learn from how open source technology has transformed other traditional industries"
  },
  {
    "href": "https://video.fosdem.org/2023/D.energy/energy_challenges_home_energy_management.webm",
    "title": "Challenges in Home Energy Management\nHow to best use your own PV-generated power"
  },
  {
    "href": "https://video.fosdem.org/2023/D.energy/energy_obstacles_to_os_in_building.webm",
    "title": "Obstacles to open source in building energy technology\nAn analysis of the German research landscape"
  },
  {
    "href": "https://video.fosdem.org/2023/D.energy/energy_everest.webm",
    "title": "EVerest: AC and DC electric vehicle charging with open source software and hardware"
  },
  {
    "href": "https://video.fosdem.org/2023/D.energy/energy_eichrecht.webm",
    "title": "European Eichrecht\nE-Mobility with Love & Security"
  },
  {
    "href": "https://video.fosdem.org/2023/D.energy/energy_seapath.webm",
    "title": "Presentation of the SEAPATH project"
  },
  {
    "href": "https://video.fosdem.org/2023/D.energy/energy_green_software_engineering.webm",
    "title": "Green software engineering\nBuilding tools and ecosystems around green software engineering"
  },
  {
    "href": "https://video.fosdem.org/2023/D.energy/energy_scheduling_kubernetes.webm",
    "title": "Carbon Intensity Aware Scheduling in Kubernetes"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/energy_welcome_oncampus_devroom.webm",
    "title": "Welcome to the on-campus Energy Devroom"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/energy_v2gliberty.webm",
    "title": "V2GLiberty: The open stack that could\nHow we enable EV owners to be ahead of the industry, with open source software"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/energy_openstef.webm",
    "title": "OpenSTEF: Open Source energy predictions"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/energy_four_years_openhab.webm",
    "title": "4 Years of Energy Management with openHAB\nA personal story about smart homes, PV systems and EVs."
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/energy_combatting_software_driven_environmental_harm.webm",
    "title": "Combatting Software-Driven Environmental Harm With Free Software"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/energy_fossil_free_internet.webm",
    "title": "Getting to a fossil free internet by 2030\nA tour of the tech and policy changes to get us there"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/energy_power_profiling_firefox.webm",
    "title": "Power profiling with the Firefox Profiler"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/energy_modeling_global_south.webm",
    "title": "Update on open-source energy system modeling in the global south and including Africa"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/energy_open_data_open_source_adoption.webm",
    "title": "Open data and open-source adoption in the energy sector\nfilling the gaps with the open community"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/beam_elixir_intro.webm",
    "title": "Elixir - Old wine in new casks\nIntro talk about Elixir/Erlang"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/beam_gleam_intro.webm",
    "title": "Introduction to Gleam\nby building type-safe Discord bots on the BEAM"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/beam_speak_binary_to_me.webm",
    "title": "Speak binary to me\nLearn the powers of binary pattern matching"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/beam_liveview_keeps_you_warm.webm",
    "title": "LiveView keeps you warm!\nBuilding a knitting machine UI with Phoenix LiveView"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/beam_distributed_music_programming_gleam.webm",
    "title": "Distributed music programming with Gleam, BEAM, and the Web Audio API"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/beam_actor_model_load_testing.webm",
    "title": "The Actor Model as a Load Testing Framework"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/beam_shorter_feedback_loops_livebook.webm",
    "title": "Shorter feedback loops with Livebook"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/beam_running_erlang_elixir_microcontrollers_atomvm.webm",
    "title": "Running Erlang and Elixir on microcontrollers with AtomVM\nHow to run BEAM code on a 3 $ microcontroller"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/beam_dealing_with_a_monster_query.webm",
    "title": "Dealing with a Monster Query\na story of Elixir & optimization"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.201/fast_data_realtime_stream_analytics_on_traces.webm",
    "title": "Running Real-time Stream Processing Analytics On Traces"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.201/fast_data_cdc_apache_flink.webm",
    "title": "CDC Stream Processing with Apache Flink\nA peek under the hood of a changelog engine"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.201/fast_data_apache_beam_streaming_analytics.webm",
    "title": "An introduction to Apache Beam for streaming analytics\nGet to know how to leverage Apache Beam for your streaming analytics pipelines"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.201/fast_data_a_million_rows_per_second_time_series_questdb.webm",
    "title": "Ingesting over a million rows per second on a single instance.\nTime-series processing using QuestDB"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.201/fast_data_realtime_dashboard_streamlit_apache_pinot_apache_pulsar.webm",
    "title": "Building A Real-Time Analytics Dashboard with Streamlit, Apache Pinot, and Apache Pulsar\nBest of Both Worlds with Event Streaming and Real-Time Analytics"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.201/fast_data_analytical_apps_with_clickhouse.webm",
    "title": "Building Analytical Apps With ClickHouse"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/appinventor.webm",
    "title": "Building Personalized AI Apps with MIT App Inventor"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/hedy.webm",
    "title": "Hedy: A gradual and multi-lingual programming language for education"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/microblocks.webm",
    "title": "MicroBlocks: small, fast, human friendly"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/snap.webm",
    "title": "Snap! - Build Your Own Blocks\nA visual programming language for Computing Education"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/lomiri.webm",
    "title": "Lomiri Mobile Linux in Desktop mode\nLomiri and the myth of the pocket size desktop computer"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/sharp_photos.webm",
    "title": "AMENDMENT Sharp photos and short movies on a mobile phone"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/mainline_on_the_fairphone4.webm",
    "title": "Mainline Linux on recent Qualcomm SoCs: Fairphone 4\nA look into the work of getting a modern Qualcomm SoC into mainline Linux."
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/mobian_to_stable_and_beyond.webm",
    "title": "Mobian: to stable... and beyond!"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/phosh.webm",
    "title": "What's new in the world of phosh?"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/ondev2_installer.webm",
    "title": "Ondev2: Distro-Independent Installer For Linux Mobile"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/sailfish.webm",
    "title": "Sailing into the Linux port with Sony Open Devices \nA journey of adapting Sailfish OS to work on Sony Xperia phones "
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/convergent_kirigami_apps.webm",
    "title": "AMENDMENT Writing a convergent application in 2023 with Kirigami"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/future_of_mobile.webm",
    "title": "Where do we go from here?\nThe future of Linux on Mobile could be exciting, scary, or both!"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/foojay.webm",
    "title": "Welcome to the Friends of OpenJDK (Foojay.io) Developer Room!"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/javapopularity.webm",
    "title": "After Nearly 30 Years, How Is Java So Popular?"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/upgrade.webm",
    "title": "Why And How To Upgrade To Java 17 (And Prepare For 21)"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/hazelcast.webm",
    "title": "Best Practices For Real-Time Stream Processing (With Hazelcast Open Source Platform)"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/dependencies.webm",
    "title": "Keep Your Dependencies In Check"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/migrations.webm",
    "title": "Major Migrations Made Easy With OpenRewrite"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/log4shell.webm",
    "title": "Rethinking Ecosystem Security After Log4Shell"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/elasticsearch.webm",
    "title": "Elasticsearch Internals"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/supplychain.webm",
    "title": "Securing Your Software Supply Chain One Open Source Project at a Time"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/miss.webm",
    "title": "What I Miss In Java (The Perspectives Of A Kotlin Developer)"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/pi.webm",
    "title": "Update on #JavaOnRaspberryPi and Pi4J"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/hardware.webm",
    "title": "Write Once, Run Anywhere... Well, What About Heterogeneous Hardware?"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/jit.webm",
    "title": "The Next Frontier in Open Source Java Compilers: Just-In-Time Compilation as a Service"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/serverless.webm",
    "title": "Afraid Of Java Cold Starts In Serverless? Fear Not, Java Is Super Fast!"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/firecracer.webm",
    "title": "FireCRaCer: The Best Of Both Worlds"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/graalvm.webm",
    "title": "Classics Never Get Old: Two Easy Pieces For GraalVM"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/asyncgetstacktrace_the_improved_version_of_asyncgetcalltrace_jep_435.webm",
    "title": "AsyncGetStackTrace: The Improved Version Of AsyncGetCallTrace (JEP 435)"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/quarkus.webm",
    "title": "Quarkus 101: Intro To Java Development With Quarkus"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/pulsar.webm",
    "title": "Modernizing Legacy Messaging System with Apache Pulsar"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/fuzion.webm",
    "title": "Fuzion — Intro for Java Developers: Mapping Java's Features to Simpler Mechanisms"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/gostateofgo.webm",
    "title": "The State of Go\nWhat's new since Go 1.19"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/goreducecognitive.webm",
    "title": "Recipes for reducing cognitive load\nyet another idiomatic Go talk"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/gocidagger.webm",
    "title": "Building a CI pipeline with Dagger in Go"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/godebugconcurrency.webm",
    "title": "Debugging concurrency programs in Go"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/godelve.webm",
    "title": "What's new in Delve / Tracing Go programs with eBPF"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/goevenfurtherwithoutwires.webm",
    "title": "Go Even Further Without Wires\nLong Distance Radio Communication Using Go and TinyGo"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/gooptimizingstrings.webm",
    "title": "Optimizing string usage in Go programs"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/gosqueezingfunction.webm",
    "title": "Squeezing a go function"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/goreconciliation.webm",
    "title": "Reconciliation Pattern, Control Theory and Cluster API: The Holy Trinity"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/gofivestepsefficient.webm",
    "title": "Five Steps to Make Your Go Code Faster & More Efficient"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/goheadscale.webm",
    "title": "Headscale: How we are using integration testing to reimplement Tailscale"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/gobuildingdatabase.webm",
    "title": "Our Mad Journey of Building a Vector Database in Go\nBuilding a Database in Go"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/gowatermill.webm",
    "title": "Building a basic event-driven application in Go in 20 minutes\nIntroduction to Watermill"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/goisoo.webm",
    "title": "Is Go Object-Oriented? A Case of Public Opinion"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/govisuallyprogramming.webm",
    "title": "Visually programming Go\nLet's mix Blockly + Go and see what happens!"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/govfkit.webm",
    "title": "vfkit - a native macOS hypervisor written in go"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/golightning.webm",
    "title": "Go Lightning talks\nCome speak!"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/graph_tedective.webm",
    "title": "TEDective\nOpening up European Public Procurement Data"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/graph_ipysigma.webm",
    "title": "ipysigma: a Jupyter widget for interactive visual network analysis"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/graph_case_for_dag.webm",
    "title": "A case for DAG databases\nCorrelating revision history with CI results"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/graph_ml_visualization.webm",
    "title": "Visualization paradigm that will (potentially) replace force layouts\nVisualization paradigm that allows an effective arrangement of the graph, through the use of AI"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/graph_grouping_zoomer.webm",
    "title": "Graph Stream Zoomer\nA window-based graph stream grouping system based on Apache Flink"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/graph_ldbc.webm",
    "title": "The LDBC Social Network Benchmark"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/graph_gephi_future.webm",
    "title": "Gephi towards v1.0: the codebase, and the rest"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/haskell_devroom_welcome.webm",
    "title": "Welcome to the Haskell devroom"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/haskell_tooling_overview.webm",
    "title": "A quick overview of the Haskell tooling"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/haskell_katas_hackathon.webm",
    "title": "Hackathon HaskellKatas style\nInstall a complete hackable haskell katas environment for a new hackathon concept"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/haskell_web_app_architecture_flora.webm",
    "title": "Web application architecture in Haskell with flora.pm\nA case study of a Haskell community platform in 2022"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/haskell_security_advisory_db.webm",
    "title": "The Haskell Security Advisory Database\nStatus and next steps"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/haskell_rust_interop.webm",
    "title": "On the path of better interoperability with Rust!"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/haskell_2d_animations.webm",
    "title": "2D animations in Haskell using gloss, lens and state"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/haskell_foundation_open_source.webm",
    "title": "Open-Source Opportunities with the Haskell Foundation"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1309%20(Van%20Rijn)/haskell_devroom_farewell.webm",
    "title": "Acknowledgements, *prize draw* and farewell"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/paraview.webm",
    "title": "Efficiently exploit HPC resources in scientific analysis and visualization with ParaView"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/straw_slurm.webm",
    "title": "Simplifying the creation of Slurm client environments\nA Straw for your Slurm beverage"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/troika_hpc_jobs.webm",
    "title": "Troika: Submit, monitor, and interrupt jobs on any HPC system with the same interface"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/k8s_rdma_openstack.webm",
    "title": "Self-service Kubernetes Platforms with RDMA on OpenStack\nK8s, OpenStack and RDMA are just like oil, vinegar and bread?"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/hpc_software_validation.webm",
    "title": "How to deal with validation as an HPC software?\nAn approach to power software testing at scale"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/lofar_foss_hpc.webm",
    "title": "LOFAR: FOSS HPC across 2000 kilometers\nThe unknown world of open source radio astronomy software"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/metahub.webm",
    "title": "HPC Container Conformance\nGuidance on how to build and annotate containers for HPC"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/ldcb_benchmark_suite.webm",
    "title": "The LDBC benchmark suite"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/gpu_multiple_double_arithmetic.webm",
    "title": "Multiple Double Arithmetic on Graphics Processing Units\nGPU acceleration to offset the cost overhead of multiple double arithmetic"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/overengineering_ml_pet_project.webm",
    "title": "Overengineering an ML pet project to learn about MLOps\nForce yourself to do pushups while working from home!"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/cpu_tuning_gnu_guix.webm",
    "title": "Reproducibility and performance: why choose?\nCPU tuning in GNU Guix"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/librsb.webm",
    "title": "LIBRSB: Universal Sparse BLAS Library\nA highly interoperable Library for Sparse Basic Linear Algebra Subroutines and more for Multicore CPUs"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/numba_mpi.webm",
    "title": "numba-mpi\nNumba @njittable MPI wrappers tested on Linux, macOS and Windows"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/toro_unikernel_mpi.webm",
    "title": "Running MPI applications on Toro unikernel"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/must_mpi_correctness_checking.webm",
    "title": "MUST: Compiler-aided MPI correctness checking with TypeART"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/link_time_call_graph_analysis.webm",
    "title": "Link-time Call Graph Analysis to facilitate user-guided program instrumentation\nAn LLVM based approach"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/spack_stat_storm.webm",
    "title": "How the Spack package manager tames the stat storm"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/spack_ci.webm",
    "title": "Keeping the HPC ecosystem working with Spack CI"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.120%20(Chavanne)/hpc_effective_testing_pipelines.webm",
    "title": "Developing effective testing pipelines for HPC applications"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/image_linux_secureboot_uki_ddi_ohmy.webm",
    "title": "Devroom kick-off talk: UKI? DDI?? Oh my!!!\nIntroducing and decoding image-based Linux terminology and concepts"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/image_linux_secureboot_dmverity.webm",
    "title": "DM-Verity Rootfs Protection\nBlockwise Hashtree"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/image_linux_secureboot_tpm.webm",
    "title": "Image-Based Linux and TPMs\nMeasured Boot, Protecting Secrets and you"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/image_linux_secureboot_new_ways_of_initrd_build.webm",
    "title": "Building initrds in a new way"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/image_linux_secureboot_ultrablue.webm",
    "title": "Ultrablue\nUser-friendly Lightweight TPM Remote Attestation over Bluetooth"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/image_linux_secureboot_converging_packages_and_images.webm",
    "title": "Converging image and package based OS updates"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/image_linux_secureboot_ubuntu_core.webm",
    "title": "Ubuntu Core: a technical overview"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/image_linux_secureboot_suse_micro_os.webm",
    "title": "openSUSE MicroOS design\nA functional read-only OS in an imperfect world"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/image_linux_secureboot_machineos.webm",
    "title": "MachineOS: a Trusted, SecureBoot Image-based Container OS"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/kotlin.webm",
    "title": "Why we ditched JavaScript for Kotlin/JS"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/doom.webm",
    "title": "Doom on the browser thanks to WebAssmebly and .Net\nOr how I ported Managed Doom to Blazor"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/ps5.webm",
    "title": "Controlling the web with a PS5 controller"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/state_machine.webm",
    "title": "Finite state machine (and some retrogaming)"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/i2p_sam.webm",
    "title": "Javascript for Privacy-Protecting Peer-to-Peer Applications\nUsage of the I2P-SAM Javascript Library: Anonymized and End-to-End Encrypted Communication"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/strong_dynamic_type_checking.webm",
    "title": "Strong Dynamic Type Checking for JavaScript\nWhere TypeScript is helpless, JavaScript Proxies come to the rescue!"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/secure.webm",
    "title": "Secure by accident\nHow performance optimisation can lead to more secure apps"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/plugins.webm",
    "title": "The problems you will have when creating a plugins system for your shiny UI project"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/vue3.webm",
    "title": "Is it time to migrate to Vue 3?\nTLDR: it depends"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/loop.webm",
    "title": "In the loop\nor: How I Learned to Stop Worrying and Love the Event Loop"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/jxr.webm",
    "title": "jxr in /engine/ - coding in WebXR on a plane\nCustom JavaScript subtset open scaffolding to spacially and textualy explore interfaces"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/npm_visualization.webm",
    "title": "Visualize the NPM dependencies city ecosystem of your node project in VR"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/microfrontends_react.webm",
    "title": "Micro-frontends in React\nUsing Webpack Module federation to break free from monoliths in UI"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/customization_ui.webm",
    "title": "Managing customization in UI library\nHow to allow customization in complex React components library. The example of MUI."
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/architecture.webm",
    "title": "A practical approach to build an open and evolvable Digital Experience Platform (DXP)"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/firefox_profiler.webm",
    "title": "Using the Firefox Profiler for web performance analysis\nCapture a performance profile. Analyze it. Share it. Make the web faster."
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/arm_hardening.webm",
    "title": "Hardening Kernel Subsystems by Architectural Capabilities"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/hybrid_netstack.webm",
    "title": "Hybrid Networking Stack Demo"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/meta_netdevices.webm",
    "title": "meta netdevices"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/mptcp_upstream.webm",
    "title": "MPTCP in the upstream kernel\nA long road that started almost 15 years ago"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/sched_tracing.webm",
    "title": "Graphing tools for scheduler tracing"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/walking_stack_without_frame_pointers.webm",
    "title": "Walking native stacks in BPF without frame pointers"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/composefs.webm",
    "title": "composefs\nAn opportunistically sharing verified image filesystem"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/erofs.webm",
    "title": "EROFS filesystem update and its future"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/sth_to_hide.webm",
    "title": "Having Something To Hide\nTrusted Key Storage in Linux"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/bpf_hashing.webm",
    "title": "Optimizing BPF hashmap and friends"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/bpf_loader.webm",
    "title": "eBPF loader deep dive"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/kernel_fps.webm",
    "title": "Hacking the Linux Kernel to get moar FPS"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/devm_kzalloc.webm",
    "title": "Don't blame devres - devm_kzalloc() is not harmful\nUse-after-free bugs in drivers and what to do about them."
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/device_support.webm",
    "title": "Rethinking device support for the long-term"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/kotlin_devroom_welcome.webm",
    "title": "Kotlin DevRoom Welcoming Remarks"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/the_state_of_kotlin.webm",
    "title": "The State of Kotlin"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/kmp_from_hello_world_to_real_world.webm",
    "title": "Kotlin Multiplatform: From “Hello World” to the Real World"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/a_mirror_without_reflection_for_kmp.webm",
    "title": "A mirror without reflection for Kotlin/Multiplatform"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/toward_better_kmp_architecture_with_di_and_ksp.webm",
    "title": "Toward better Kotlin Multiplatform architecture with Dependency Injection and KSP"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/krump_kotlin_rust_kmp.webm",
    "title": "KRuMP - Kotlin-Rust-Multiplatform?!\nHow to write bugs once and ship them to many platforms."
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/kmp_for_android_and_ios_library_developers.webm",
    "title": "Kotlin Multiplatform for Android & iOS library developers\nTips for writing Kotlin Multiplatform Android/iOS libraries"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/functional_fun_in_kotlin.webm",
    "title": "Functional fun in Kotlin\nA 20 minute run through modern FP in Kotlin"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/be_pushy_lets_join_for_wider_and_better_kotlin.webm",
    "title": "Be pushy! Let's join for wider and better Kotlin support worldwide"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/how_we_moved_sdks_to_kmp.webm",
    "title": "How we moved SDKs to Kotlin Multiplatform\nand saved the world (kind of)."
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/improving_the_devx_in_koin_32.webm",
    "title": "Improving the Kotlin Developer Experience in Koin 3.2"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/shrinking_in_the_age_of_kotlin.webm",
    "title": "Shrinking in the Age of Kotlin"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/20_minutes_from_zero_to_live_chatbot_with_tock.webm",
    "title": "20 minutes from zero to a live chatbot with Tock"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/take_your_shot_of_vitamin.webm",
    "title": "Take your shot of Vitamin!"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/how_to_test_your_compose_ui.webm",
    "title": "How to Test Your Compose UI"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.230/kotlin_devroom_closing.webm",
    "title": "Kotlin DevRoom Closing Remarks"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/welcome_legal_policy.webm",
    "title": "Welcome to the Legal and Policy Issues Devroom"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/saass.webm",
    "title": "A Service as a Software Substitute (SaaSS) is unjust like proprietary software\nThinking carefully about services"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/windows_tax_refund.webm",
    "title": "Windows and Office \"tax\" refund\nVarious cases about the refund of pre-installed software, and the right to install any software on any device"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/foss_law.webm",
    "title": "Fuzzy Law-gic: FOSS & the Unauthorized Practice of Law"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/role_eu_open_source.webm",
    "title": "Is “European open source” a thing?\nDebating the role of open source in building Europe’s digital sovereignty"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/financing_open_source.webm",
    "title": "Financing Open Source by small companies\nWe give Open Source projects 1% of the revenue, and you can too!"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/license_review.webm",
    "title": "Open Source Initiative - Changes to License Review Process"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/learning_to_improve.webm",
    "title": "Learning From the Big Failures To Improve FOSS Advocacy and Adoption\nHow Are Big Companies Benefiting So Much from FOSS, and Individuals So Little?"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/app_store_changes.webm",
    "title": "Reckoning with new app store changes: Is now our chance?\nRecent legal and policy developments around app stores and what they mean for free software"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/administration_foss.webm",
    "title": "How to get public administrations to use more FOSS"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/eu_app_stores.webm",
    "title": "EU alternative to app stores"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/ai_discussion.webm",
    "title": "AI Discussion"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/eu_patents.webm",
    "title": "The coming EU Standard-Essential Patents regulation"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/licenses_for_standards.webm",
    "title": "The Professional's Guide To Haphazardly Picking Licenses For Standards & Specifications\nPractical tips for the reckless licensor"
  },
  {
    "href": "https://video.fosdem.org/2023/UB5.132/legal_hot_topics.webm",
    "title": "Panel: Hot Topics\nOrganizers of the Legal & Policy DevRoom discuss the issues of the day"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_migrating.webm",
    "title": "Migrating to LibreOffice Technology - old and new motivations and challenges"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_funproject.webm",
    "title": "Fun project by design – How LibreOffice development can be full of flow?\nThe ten funniest moments of my recent Numbertext, LibreLogo, Hunspell & LibreOffice developments"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_smartart.webm",
    "title": "SmartArt Support for LibreOffice"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_qadashbord.webm",
    "title": "Putting the R in LibreOffice: a Shiny dashboard for QA\nUsing R and the Shiny framework to help the LibreOffice QA community"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_unittest.webm",
    "title": "Cleaning up the unittest code mess"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_crashtesting.webm",
    "title": "Crashtesting LibreOffice in the backyard"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_darkmodes.webm",
    "title": "LibreOffice Dark Modes\nmulti-platform support was surprisingly difficult"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_elephant.webm",
    "title": "Turbocharging an elephant. Making Libreoffice faster."
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_featurelocking.webm",
    "title": "Feature Locking and Feature Restriction\nIntegrator's way to unlock potential"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_interoperability.webm",
    "title": "An Interoperability Improvement in LibreOffice Impress Tables"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_writercontent.webm",
    "title": "Writer Content Controls -- what happened in the past half year"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_footnotes.webm",
    "title": "Footnotes in multi-column sections"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_odftoolkit.webm",
    "title": "News from the ODF Toolkit\nQuick overview: Intro, use cases & updates from the past months and likely future!"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/libreoffice_graphics_subsystems_systemspecificrenderers.webm",
    "title": "LibreOffice graphics subsystems - SystemSpecificRenderers\nProviding a working Example and report about progress/findings during development"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_pdfaccessibility.webm",
    "title": "Improvements to LibreOffice PDF accessibility\nCome to see what improvements we made to PDF/UA support in LibreOffice"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_oldgraphicformats.webm",
    "title": "Supporting old proprietary graphic formats"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_libreofficekit.webm",
    "title": "LibreOfficeKit – bridge between your application and LibreOffice"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_coollockdown.webm",
    "title": "Collabora Online over lock-down\nHow LibreOffice technology in the browser got better"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_wasmport.webm",
    "title": "A Rocket Engine for LibreOffice Templates\nCome to see what's in store for the recently-moved WollMux forms and templating engine extension for LibreOffice"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_coolyours.webm",
    "title": "Make Collabora Online yours\nCustomize and integrate it everywhere"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_marryingcoolwasm.webm",
    "title": "Marrying Collabora Online and LibreOffice WASM\nRunning Collabora Online in WASM"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_coolwasm01.webm",
    "title": "Collabora Online and WASM\nAssembling off-line Collabora Online with the Web."
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/lotech_toolchain.webm",
    "title": "State of the Toolchain"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/compilerrt.webm",
    "title": "Demystifying compiler-rt-sanitizers for multiple architectures"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/syclclang.webm",
    "title": "Defining a multi-architecture interface for SYCL in LLVM Clang"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/mlirdialect.webm",
    "title": "How to Build your own MLIR Dialect"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/llvmparcoach.webm",
    "title": "Case study of creating and maintaining an analysis and instrumentation tool based on LLVM: PARCOACH"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/llvmc2.webm",
    "title": "The C2 compiler\nHow the C2 compiler evolved"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/llvmflang.webm",
    "title": "Flang progress update"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/llvmembedded.webm",
    "title": "Open source C/C++ embedded toolchains using LLVM"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/major_mariadb.webm",
    "title": "New Year -> New major-major version of MariaDB"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/mariadb_contributions.webm",
    "title": "An introduction to MariaDB contributions"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/deploying_galera.webm",
    "title": "Deploying Galera Cluster in the real world"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/new_analytics_mariadb.webm",
    "title": "What is new in analytics for MariaDB"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/data_in_use_encryption_mariadb.webm",
    "title": "Data-in-use Encryption with MariaDB"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/innodb_change_buffer.webm",
    "title": "InnoDB change buffer: Unsafe at any speed\nThe tale of some corruption bugs and how they were found"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/mysql8_mariadb1011.webm",
    "title": "MySQL 8 vs MariaDB 10.11"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/deep_dive_mysql_perf.webm",
    "title": "Deep Dive into MySQL Query Performance"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/schema_change_tidb.webm",
    "title": "Online schema change at scale in TiDB\nHow does schema changes work in a distributed SQL database"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/life_query_vitess.webm",
    "title": "Life of a Query in Vitess\nImpersonating a monolithic database"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/on_tthe_road_mysql.webm",
    "title": "On the road to managed databases"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/proxysql_lower_isolation.webm",
    "title": "Lower your isolation level with ProxySQL\nAdapt your Galera cluster setup to your needs using ProxySQL"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/hack_mysql_component.webm",
    "title": "Extending MySQL with component infrastructure\nwill MySQL be out of space soon ?"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/mysql_procfs_udf.webm",
    "title": "Extended observability to agentless monitoring on MySQL using ProcFS UDF plugin"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/welcome_to_the_matrix_devroom.webm",
    "title": "AMENDMENT Welcome to the Matrix Devroom"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/matrix_beyond_im.webm",
    "title": "AMENDMENT matrixRTC | Matrix beyond Instant Messaging\nElement Call, Scaling, Thirdroom"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/matrix_clients_as_good_as_youd_expect.webm",
    "title": "AMENDMENT Clients as good as you'd expect\nSliding-Sync, Rust-SDK & WYSIWYG"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/widgets_sovereign_workplace_german_public_sector.webm",
    "title": "AMENDMENT Widgets in the \"Sovereign Workplace\" for the German public sector"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/trixnity_one_sdk_for_almost_everything.webm",
    "title": "Trixnity\nOne Matrix SDK for (almost) everything written in Kotlin"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/bridging_ap_with_kazarma.webm",
    "title": "Bridging ActivityPub with Kazarma\nInteroperability and \"beyond-chat\" Matrix"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/all_your_base_are_belong_to_us.webm",
    "title": "All your base are belong to us\nA crazy ride through lots of matrix projects"
  },
  {
    "href": "https://video.fosdem.org/2023/D.matrix/synapse_k8s_operator.webm",
    "title": "Introduction to the Synapse Kubernetes Operator\nA new way to deploy Synapse and its Bridges on Kubernetes"
  },
  {
    "href": "https://video.fosdem.org/2023/D.matrix/cascaded_selective_forwarding_units.webm",
    "title": "Cascaded Foci (SFUs)\nSelective Forwarding Units"
  },
  {
    "href": "https://video.fosdem.org/2023/D.matrix/building_a_social_app_on_top_of_matrix.webm",
    "title": "Building a social app on top of Matrix\nFighting surveillance capitalism for fun and profit"
  },
  {
    "href": "https://video.fosdem.org/2023/D.matrix/decentralising_moderation.webm",
    "title": "Decentralizing moderation\nMjölnir for all"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/microkernel2023.webm",
    "title": "The Microkernel Landscape in 2023\nNewcomers, regulars, late bloomers, elders, oddballs and others"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/ddtransplant.webm",
    "title": "Device driver gardening\nTransplant Linux drivers fast but gently"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/genode.webm",
    "title": "Using Genode as an enabler for research on modern operating systems"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/nova.webm",
    "title": "NOVA Microhypervisor Feature Update"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/osvevolution.webm",
    "title": "Evolution of OSv: Towards Greater Modularity and Composability"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/heliosuk.webm",
    "title": "Introducing Helios Micokernel\nA small, practical microkernel"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/unikraft.webm",
    "title": "Unikraft Weather Report\nThe Unikraft Project During 2022"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/appunikraft.webm",
    "title": "Building a Linux-compatible Unikernel\nHow your application runs with Unikraft"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/hwacceluk.webm",
    "title": "Hardware acceleration for Unikernels\nA status update of vAccel"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/rustunikernel.webm",
    "title": "A Rust-Based, modular Unikernel for MicroVMs\nRustyHermit @ FOSDEM 2023"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1308%20(Rolin)/loupe.webm",
    "title": "Loupe: Designing Application-driven Compatibility Layers in Custom Operating Systems"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/db.webm",
    "title": "Monitor your databases with Open Source tools"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/postgres.webm",
    "title": "Observability in Postgres\nThe Good, the Bad, and the Ugly"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/apm.webm",
    "title": "Application Monitoring with Grafana and OpenTelemetry"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/tracing.webm",
    "title": "Practical introduction to OpenTelemetry tracing"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/kubernetes.webm",
    "title": "Exploring the power of OpenTelemetry on Kubernetes"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/api.webm",
    "title": "Observe your API with an API Gateway Plugins"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/profiling.webm",
    "title": "Adopting continuous-profiling: Understand how your code utilizes cpu/memory\nIntroduction into continuous-profiling and how it can help you writing more efficient code"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/loki.webm",
    "title": "Loki: Logging, but make it cloud native\nGet started with Loki, self dubbed \"Prometheus, but for logs\""
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/toolkit.webm",
    "title": "The O11y toolkit\nA toolkit to improve, augment and debug your Prometheus stack"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/ebpf.webm",
    "title": "Inspektor Gadget: An eBPF Based Tool to Observe Containers"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/operator.webm",
    "title": "Best Practices for Operators Monitoring and Observability in Operator SDK"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.252A%20(Lameere)/lightning.webm",
    "title": "Lightning Talks\nNetXMS | Parca | OpenSearch"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/mozilla_firefox_energy_use.webm",
    "title": "Understanding the energy use of Firefox\nWith less power comes more sustainability"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/what_is_new_firefox_profiler.webm",
    "title": "What's new with the Firefox Profiler\nPower tracks, UI improvements, importers"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/mozilla_anti_tracking.webm",
    "title": "Over a decade of anti-tracking work at Mozilla"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/mozilla_digital_service_act.webm",
    "title": "The Digital Services Act 101\nWhat is it and why should you care"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/mozilla_cachetheworld.webm",
    "title": "Cache The World\nAdventures in A11Y Performance"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/mozilla_firefox_profiler_beyond_the_web.webm",
    "title": "Firefox Profiler beyond the web\nUsing Firefox Profiler to view Java profiling data"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/mozilla_localize_your_project_with_pontoon.webm",
    "title": "Localize your open source project with Pontoon"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.220%20(Guillissen)/mozilla_intmessageformat.webm",
    "title": "The Road to Intl.MessageFormat"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/network_welcome.webm",
    "title": "Welcome to the Network devroom"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/network_p2p_browser_connectivity.webm",
    "title": "Peer-to-peer Browser Connectivity\nLeveraging WebRTC and the new WebTransport protocol to connect libp2p browser nodes."
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/network_snabbflow_ipfix.webm",
    "title": "Snabbflow: a scalable IPFIX exporter\nA tour of the IPFIX exporter developed at SWITCH"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/network_ids_in_2023.webm",
    "title": "What is an IDS and Network Security Monitoring in 2023?\nMonitoring, Detection, challenges and solutions while chasing APTs, CVEs and Ransomware."
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/network_ddos_detection.webm",
    "title": "DDoS attack detection with open source FastNetMon Community"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/network_ntopng_event_driven_analysis.webm",
    "title": "ntopng: an actionable event-driven network traffic analysis application\nHow ntopng can be used as a scriptable system capable of reacting to network events."
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/network_time_sensitive.webm",
    "title": "So you want to build a deterministic networking system\nA gentle introduction to Time Sensitive Networking"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/network_hole_punching_in_the_wild.webm",
    "title": "Hole punching in the wild\nLearnings from running libp2p hole punching in production, measured from vantage points across the globe."
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/network_cni_unleashed.webm",
    "title": "\"CNI Unleashed\"\nHow to deal with CNI plugin chains."
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/network_management.webm",
    "title": "Networking management made simple with Nmstate\nTaming the internals of NetworkManager"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/network_wifi_mesh.webm",
    "title": "prplMesh: open source Wi-Fi mesh\nSolving home Wi-Fi"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/network_service_mesh.webm",
    "title": "Service MESH without the MESS\nLatest of eBPF Powered Cilium Service Mesh"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/network_metallb_and_frr.webm",
    "title": "MetalLB and FRR: a match made in heaven"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/network_decentralized_storage.webm",
    "title": "Decentralized Storage with IPFS\nHow does it work under the hood?"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/network_cni_automagic.webm",
    "title": "CNI Automagic: Device discovery for semantic network attachment in Kubernetes"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/network_cilium_and_grafana.webm",
    "title": "Golden Signals with Cilium and Grafana"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/network_pods_to_multiple_networks.webm",
    "title": "Need to connect your k8s pods to multiple networks? No problem [with calico/vpp]!\nMulti-legged containers running wild with calico/vpp"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/nix_and_nixos_welcome.webm",
    "title": "Welcome to the Nix and NixOS devroom"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/nix_and_nixos_i_am_excited_about_nixos.webm",
    "title": "I am excited about NixOS, I want to tell you why!"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/nix_and_nixos_make_anyone_use_nix.webm",
    "title": "Make Anyone Use Nix\n\"It'll be fine\"TM"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/nix_and_nixos_nixel.webm",
    "title": "Nixel: a nicer way to write your Nix expressions"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/nix_and_nixos_playing_with_nix_in_hpc_environments.webm",
    "title": "Playing with Nix in adverse HPC environments"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/nix_and_nixos_contracts_for_free.webm",
    "title": "Contracts for free!"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/nix_and_nixos_devenv.webm",
    "title": "devenv.sh - Fast, Declarative, Reproducible, and Composable Developer Environments"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/nix_and_nixos_development_process.webm",
    "title": "The Nix package manager development process"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/nix_and_nixos_runix.webm",
    "title": "Runix\na type-safe Rust interface to the Nix CLI"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/nix_and_nixos_p4_in_nix.webm",
    "title": "P4 in Nix\nBringing hardware accelerated network to the masses!"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/nix_and_nixos_towards_secure_boot.webm",
    "title": "Towards Secure Boot for NixOS"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/nix_and_nixos_a_success_story.webm",
    "title": "A success story of adopting Nix at a workplace\nFrom reproducible CI builds to production"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/om_gstreamer.webm",
    "title": "GStreamer: State of the Union 2023"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/om_pipewire.webm",
    "title": "PipeWire state of the union\nWhat is and what will be"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/om_chromium.webm",
    "title": "Modern Camera Handling in Chromium\nImplementing Camera Access with xdg-desktop-portal and PipeWire in Chromium"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/om_liquidsoap.webm",
    "title": "Advanced programmable use of Liquidsoap with FFmpeg\nExplore how the liquidsoap language can be used in new, safe ways for building media pipelines and leverage FFmpeg functionalities"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/om_vlc.webm",
    "title": "Dual presentation: FFmpeg 6 and VLC.js"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/om_av1.webm",
    "title": "4K HDR video with AV1 : A Reality Check"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/om_vvc.webm",
    "title": "VVenC & VVdeC: Open source video encoding and playback for VVC\nH.264/AVC – x264, H.265/HEVC – x265, H.266/VVC – VVenC? History, current state, and ecosystem around open source VVC implementations."
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/om_ffv1.webm",
    "title": "The FFV1 ecosystem\nA lossless video coding format. IETF standardization, FFmpeg, MediaConch, RAWcooked"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/om_avx512.webm",
    "title": "AVX512 in FFmpeg"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/om_rvv_sve2.webm",
    "title": "Scalable vector multimedia optimisations\nRVV and SVE2 extension intro"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/om_fim.webm",
    "title": "Using the FIM (Fbi IMproved) Universal Image Viewer\nA scriptable and highly configurable, yet minimalistic image viewer for X, the Linux framebuffer, and Ascii Art, for command line users"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/om_webrtc.webm",
    "title": "Merging Two Worlds - Broadcast and WebRTC"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/om_animation.webm",
    "title": "The open source stack for animation movie pipelines\nThe tools needed to cover every step of the animation movie creation process"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/om_melrose.webm",
    "title": "Melrōse, a music programming environment\nnew language to program MIDI sequences"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/om_music.webm",
    "title": "Become a rockstar using FOSS!\nOr at least use FOSS to write and share music for fun!"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/om_virt.webm",
    "title": "Distributing multicast channels to 3rd parties: a case study with OSS and virtualization/SR-IOV"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/openresearch_relativitization.webm",
    "title": "Relativitization: an interstellar social simulation framework and a turn-based strategy game"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/openresearch_muphyn.webm",
    "title": "MuPhyN - MultiPhysical Nexus\nAn academic simulation tools based on Python toolboxes"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/openresearch_guix.webm",
    "title": "Guix, toward practical transparent, verifiable and long-term reproducible research"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/openresearch_under_equipped_social_scientist.webm",
    "title": "The under-equipped social scientist ?\nWhy do we need more dedicated, flexible and documented Python libraries for social sciences."
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/openresearch_noisecapture.webm",
    "title": "Preliminary analysis of crowdsourced sound data with FOSS"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/openresearch_tackling_disinformation.webm",
    "title": "Tackling disinformation using opensource software\nTha case of Qactus"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/openresearch_pimmi.webm",
    "title": "PIMMI\nPython IMage MIning"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/openresearch_research_data_control.webm",
    "title": "AMENDMENT Better engineer-researcher collaborations though data control"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/openresearch_cortext.webm",
    "title": "CorTexT Manager, a growing online platform in open research for social sciences"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/openresearch_twitter_explorer.webm",
    "title": "Interactive network visualizations as \"guided close reading\" devices for the social sciences\nDevelopment of the twitter-explorer"
  },
  {
    "href": "https://fosdem.org/2023/schedule/event/openresearch_webmapping_massive_stats/",
    "title": "Webmapping and massive statistical data, a democratization story"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/openresearch_webmapping_massive_stats.webm",
    "title": "Webmapping and massive statistical data, a democratization story"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/openresearch_webmapping_massive_stats.mp4",
    "title": "Webmapping and massive statistical data, a democratization story"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/openresearch_executable_papers.webm",
    "title": "Executable papers in the Humanities, or how did we land to the Journal of Digital History"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/openresearch_turing_way.webm",
    "title": "The Turing Way: Changing research culture through open collaboration"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/open_research_open_panel.webm",
    "title": "Open Research Open Panel\nOpen discussion among the open research tools and technologies community"
  },
  {
    "href": "https://video.fosdem.org/2023/D.research/openresearch_software_sustainability_institute.webm",
    "title": "The Software Sustainability Institute Community and Events\nHow the SSI supports research software through community-building and events"
  },
  {
    "href": "https://video.fosdem.org/2023/D.research/openresearch_rse_asia_association.webm",
    "title": "Establishing the Research Software Engineering (RSE) Asia Association with the Open Life Science programme"
  },
  {
    "href": "https://video.fosdem.org/2023/D.research/openresearch_fairpoints.webm",
    "title": "FAIRPoints"
  },
  {
    "href": "https://video.fosdem.org/2023/D.research/openresearch_frictionless_application.webm",
    "title": "Frictionless Application (IDE for CSV)"
  },
  {
    "href": "https://video.fosdem.org/2023/D.research/openresearch_papis.webm",
    "title": "Papis: a simple, powerful and extendable command-line bibliography manager"
  },
  {
    "href": "https://video.fosdem.org/2023/D.research/openresearch_wikimedia.webm",
    "title": "Research at the service of free knowledge: Building open tools to support research on Wikimedia projects"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/penpot_official_launch.webm",
    "title": "Penpot official launch!\nWe made it! We're ready for our breaking moment!"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/value_driven_design.webm",
    "title": "Value driven design\nA case study on a successful privacy by design project where we did everything wrong"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/donation_page_design.webm",
    "title": "Donation Page Design\nHelping your users help you"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/creative_freedom_summit_retrospective.webm",
    "title": "Creative Freedom Summit Retrospective"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/accessibility_and_open_source.webm",
    "title": "Accessibility & Open Source\nHow open source is key to building a more inclusive world."
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/a11y_eaa_bfsg_wcag_wai_aria_wtf.webm",
    "title": "A11y: EAA, WCAG, WAI, ARIA, WTF? – it’s for the people stupid!\nThe web is already accessible – it's us as developers who are including barriers. Let's make the web accessible together."
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/building_a_ux_research_toolkit.webm",
    "title": "Building a UX Research toolkit\nHow a UX Research Toolkit is being built for the Open Source Ecosystem"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/practical_ux_at_openproject.webm",
    "title": "Practical UX at OpenProject\nMusing after 1½ years of working on the UX of open source software"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.201/osf_amd_4th.webm",
    "title": "Open Source Firmware status on AMD platforms 2023 - 4th edition\nOSF on AMD 4th edition"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.201/heads_status_update.webm",
    "title": "Heads - status update!"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.201/arm_secure_boot_2.webm",
    "title": "Overview of Secure Boot state in the ARM-based SoCs\n2nd edition"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.201/twpm_osf_tpm.webm",
    "title": "Trustworthy Platform Module\nAn attempt to create open-source firmware for TPM"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.201/semihosting_uboot.webm",
    "title": "Semihosting U-Boot\nLook, ma, no serial!"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/rot_opening.webm",
    "title": "Opening Railways and Open Transport devroom"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/rot_osrd.webm",
    "title": "Automated short-term train planning in OSRD"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/rot_rcmdx.webm",
    "title": "Using open source software to boost measurement data in railways"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/rot_motis.webm",
    "title": "Introducing MOTIS Project\nAn Open Source Door-to-Door Routing Platform"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/rot_transition.webm",
    "title": "Transit network planning for everyone\noptimise your network, reduce transit time for users!"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/rot_digitransit.webm",
    "title": "Digitransit\nAn open-source journey planning project"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/rot_opentripplanner.webm",
    "title": "OpenTripPlanner\npast, present and the future"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/rot_navitia.webm",
    "title": "Developing open transport toolbox and community for ten years\nFrom open data, via Navitia, to Open transport meetups, looking in the rear view mirror"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/rot_kitinerary.webm",
    "title": "Public Transport Data in KDE Itinerary\nQuerying realtime journey data and dissecting ticket barcodes"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/rot_osm.webm",
    "title": "OpenStreetMap, one geographic database to rule them all?\nMapping the railway network for the public, with the public"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.126/rot_closing.webm",
    "title": "Closing Railways and Open Transport devroom"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/postgresql_tour_de_data_types_varchar2_or_char_255.webm",
    "title": "Tour de Data Types: VARCHAR2 or CHAR(255)?"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/postgresql_how_to_give_your_postgres_blog_posts_an_outsize_impact.webm",
    "title": "How to Give Your Postgres Blog Posts an Outsize Impact"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/postgresql_when_it_all_goes_right.webm",
    "title": "When it all GOes right"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/postgresql_the_human_factor_why_database_teams_need_crew_resource_management.webm",
    "title": "AMENDMENT The Human Factor: Why Database teams Need Crew Resource Management"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/postgresql_bulk_inserts_with_postgresql_four_methods_for_efficient_data_loading.webm",
    "title": "Bulk Inserts With PostgreSQL: Four Methods For Efficient Data Loading"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/postgresql_dba_evolution_the_changing_role_of_the_database_administrator.webm",
    "title": "DBA Evolution (the Changing Role of the Database Administrator)"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/postgresql_deep_dive_into_query_performance.webm",
    "title": "Deep Dive Into Query Performance"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/postgresql_dont_do_this.webm",
    "title": "Don't Do This"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/publiccode_dpg_intro.webm",
    "title": "AMENDMENT Intro to public code and Digital Public Goods"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/publiccode_dpg_covid_exposure.webm",
    "title": "AMENDMENT Covid Exposure Notification Out in the Open\nDeveloping an Open Implementation of the Google/Apple Exposure Notification Protocol"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/publiccode_dpg_qa_emergency_supplies.webm",
    "title": "AMENDMENT Global Open Source Quality Assurance of Emergency Supplies"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/publiccode_dpg_public_money.webm",
    "title": "AMENDMENT Public Money? Public Code! in Europe\nA policy brief of the state of play of Free Software in the European Union"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/publiccode_dpg_full_stack_dpgs.webm",
    "title": "The “Full-Stack DPGs”\nBuild open, build early, build right."
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/publiccode_dpg_eu_interoperable_europe.webm",
    "title": "AMENDMENT The New EU Interoperable Europe Act and the Reuse of Software in Public Administration\nImplications for OSS in Public Administrations"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/python_telegram_bot.webm",
    "title": "An introduction to async programming\nWriting a Telegram Antispam Bot in Python"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/python_faster_serialization.webm",
    "title": "Accelerating object serialization by using constraints\nHow we achieved 3x-100x faster data serialization to a binary format or to JSON using low-level Cython and Python C API."
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/python_install_malware.webm",
    "title": "pip install malware"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/python_semantic_search.webm",
    "title": "Building a Semantic Search Application in Python, Using Haystack"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/python_build_event_driven_application.webm",
    "title": "How to build an event-driven application in Python\nA practical tutorial for building an event-driven, distributed food delivery app using microservices, kubernetes, mongodb, and a message broker in python."
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/python_micropython_intro.webm",
    "title": "An introduction to MicroPython"
  },
  {
    "href": "https://video.fosdem.org/2021/D.python/python_reloading.webm",
    "title": "AMENDMENT Code reloading techniques in Python\nCold and hot code reloading, the different options, how they work and when to use them."
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/python_hacking_esp32.webm",
    "title": "Realtime 3D Graphics on a MicroPython ESP32\nHacking the EMFCamp Conference Badge"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/python_music_recommendation.webm",
    "title": "Simple, open, music recommendations with Python"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/python_duckdb.webm",
    "title": "DuckDB: Bringing analytical SQL directly to your Python shell."
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/python_continuous_documentation.webm",
    "title": "Continuous Documentation for Your Code"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/python_dasbus.webm",
    "title": "Talk to DBus from a Python application\nAn introduction to the dasbus library"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/python_logging.webm",
    "title": "Python Logging Like Your Job Depends on It\nA fast track to understanding logging in Python"
  },
  {
    "href": "https://video.fosdem.org/2023/UD2.218A/python_pyscript.webm",
    "title": "Will PyScript replace Django?\nWhat PyScript is and is not"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/w3c_update.webm",
    "title": "W3C RTC Working Group Update "
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/media_streaming_mesh.webm",
    "title": "Media Streaming Mesh\nReal-Time Media in Kubernetes"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/modern_xmpp_auth.webm",
    "title": "Modernizing Authentication and Authorization in XMPP\nIt's time to forget your password..."
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/opensips.webm",
    "title": "OpenSIPS 3.3 – Messaging in the IMS and UC ecosystems"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/cgrates.webm",
    "title": "Build your own Real Time Billing using CGRateS"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/voip_performance.webm",
    "title": "Performance optimization for VoIP services"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/janus.webm",
    "title": "Social audio applications with Janus\nUsing WebRTC broadcasting for more than just video"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/jitsi_p10k.webm",
    "title": "P10K: getting 10000 participants into a Jitsi meeting\nHow we leveraged XMPP and the tricks we are using to get to 10000 participants"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/edge_rtc_observability.webm",
    "title": "Edge observability for RTC apps\nintroducing qryn, the polyglot monitoring and observability stack"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/webrtc_dev_trends.webm",
    "title": "Quantitative Analysis of Open Source WebRTC Developer Trends"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/secure_voip_payments.webm",
    "title": "Secure payments over VoIP calls in the cloud\nHow to architect an oncall live payment system in the cloud using Kamailio & RTP Engine."
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/interoperable_chat.webm",
    "title": "Interoperable Chat, Dutch Healthcare and the Digital Markets Act\nAbout the pitfalls of interoperable chat"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/linphone_sfu.webm",
    "title": "Real-time audio/video conferences in Linphone thanks to a modern SFU server"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.401/scaling_rtc_messaging.webm",
    "title": "Scaling Open Source Realtime Messaging System for Millions"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/rv_selfhosting_all_the_way_down.webm",
    "title": "Self-Hosting (Almost) All The Way Down\nA FPGA-based Fedora-capable computer that can rebuild its own bitstream"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/rv_qtrvsim.webm",
    "title": "QtRVSim—Education from Assembly to Pipeline, Cache Performance, and C Level Programming"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/rv_gnu_guix.webm",
    "title": "Porting RISC-V to GNU Guix\nA year in review"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/rv_gentoo.webm",
    "title": "Linux on RISC-V\nStatus and progress of RISC-V support in Gentoo Linux and other Linux distributions"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/rv_gcc_builtin.webm",
    "title": "How to add an GCC builtin to the RISC-V compiler"
  },
  {
    "href": "https://video.fosdem.org/2023/K.4.601/rv_openhw.webm",
    "title": "Bringing up the OpenHW Group RISC-V tool chains"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/building_an_actor_library_for_quickwits_indexing_pipeline.webm",
    "title": "Building an actor library for Quickwit's indexing pipeline."
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/rust_building_a_distributed_search_engine_with_tantivy.webm",
    "title": "Building a distributed search engine with tantivy\nHow lnx is solving the challenges of builing a distributed search engine in Rust"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/rust_aurae_a_new_pid_1_for_distributed_systems.webm",
    "title": "Aurae: Distributed Runtime\nA new node init system written in Rust"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/rust_bastionlab.webm",
    "title": "Presentation of BastionLab, a Rust open-source privacy framework for confidential data science collaboration\nThe reason of why Rust is the most appropriate language for our project"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/rust_neovim_and_rust_analyzer_are_best_friends.webm",
    "title": "Neovim and rust-analyzer are best friends"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/rust_a_rusty_cheri_the_path_to_hardware_capabilities_in_rust.webm",
    "title": "A Rusty CHERI - The path to hardware capabilities in Rust\nA status report on ongoing efforts to support CHERI architectures in Rust"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/rust_slint_are_we_gui_yet.webm",
    "title": "Slint: Are we GUI yet?"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/rust_rust_api_design_learnings.webm",
    "title": "Rust API Design Learnings\nLessons learned from building Rust libraries"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/rust_a_deep_dive_inside_the_rust_frontend_for_gcc.webm",
    "title": "A deep dive inside the Rust frontend for GCC"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/rust_merging_process_of_the_rust_compiler.webm",
    "title": "Merging process of the rust compiler"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/rust_lets_write_snake_game.webm",
    "title": "Let's write Snake game!\nUsing Bevy engine, we will code together a snake game from scratch"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/rust_glidesort.webm",
    "title": "Glidesort\nEfficient In-Memory Adaptive Stable Sorting on Modern Hardware"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/rust_how_pydantic_v2_leverages_rusts_superpowers.webm",
    "title": "How Pydantic V2 leverages Rust's Superpowers\nUsing Rust to build Python extensions"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/rust_scalable_graph_algorithms_in_rust_and_python.webm",
    "title": "Scalable graph algorithms in Rust (and Python)"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/rust_using_rust_for_your_network_management_tools.webm",
    "title": "Using Rust for your network management tools!\nLet the crabs control the packets!"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/rust_backward_and_forward_compatibility_for_security_features.webm",
    "title": "Backward and forward compatibility for security features"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1302%20(Depage)/rust_atuin_magical_shell_history_with_rust.webm",
    "title": "atuin: magical shell history with Rust\nuseful shell history on all of your machines"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/security_remote_fido.webm",
    "title": "Enabling FIDO2/WebAuthn support for remotely managed users"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/security_fido_beyond.webm",
    "title": "FIDO beyond the browser"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/security_fapolicyd.webm",
    "title": "AMENDMENT Hardening Linux System with File Access Policy Daemon"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/security_elliptic_curves_in_foss.webm",
    "title": "Elliptic curves in FOSS\nMore curves to the set"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/security_fips_in_openssl.webm",
    "title": "OpenSSL in RHEL: FIPS-140-3 certification\nFrom FIPS-140-2 upstream to FIPS-140-3 downstream"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/security_kerberos_pkinit.webm",
    "title": "Kerberos PKINIT: what, why, and how (to break it)"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/security_keylime.webm",
    "title": "Remote Attestation with Keylime"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/security_hpke_pq.webm",
    "title": "AMENDMENT Hybrid Public Key Encryption in PQ world?\nConverting HPKE to be PQ"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/security_where_does_that_code_come_from.webm",
    "title": "Where does that code come from?\nGit Checkout Authentication to the Rescue of Supply Chain Security"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/security_whom_do_you_trust.webm",
    "title": "Whom Do You Trust?\nPrivacy and Collaboration in CryptPad"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/security_rugby_sigstore.webm",
    "title": "What Does Rugby Have To Do With Sigstore?\nLearning Sigstore via Rugby"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/security_crowdsec.webm",
    "title": "How to protect your Kubernetes cluster using Crowdsec"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/security_linphone.webm",
    "title": "Secure voice/video over IP communications today and tomorrow thanks to post-quantum encryption !\nThe Linphone softphone has integrated CRYSTALS-Kyber, the NIST finalist algorithm in the encryption key category"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/security_mercator.webm",
    "title": "Mercator\nMapping the information system"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/security_hw_backed_attestation.webm",
    "title": "Hardware-backed attestation in TLS"
  },
  {
    "href": "https://video.fosdem.org/2023/UA2.118%20(Henriot)/security_stackrox.webm",
    "title": "Demystifying StackRox\nUnlock zero trust cloud-native security in Kubernetes"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/sbom_welcome.webm",
    "title": "Welcome to the SBOM devroom!\nIntroduction to the devroom"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/sbom_ort.webm",
    "title": "Generating SBOM made easy with ORT"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/sbom_sw360.webm",
    "title": "Understanding and Managing the Dependency in SBOM with the New Feature of SW360"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/sbom_yocto_agl.webm",
    "title": "AMENDMENT: SBOM with the Yocto Project for Automotive Grade Linux\nIntro and lessons learned"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/sbom_openembedded_yocto.webm",
    "title": "AMENDMENT: Automated SBoM generation with OpenEmbedded and the Yocto Project\nA case study of automated SBoM generation in meta build systems"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/sbom_hermine.webm",
    "title": "Hermine: converting SBOMS into legal obligations"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/sbom_siemens.webm",
    "title": "A standard BOM for Siemens"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/sbom_fossology.webm",
    "title": "FOSSology and SPDX\nHow FOSSology works with SPDX"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/sbom_build_recorder.webm",
    "title": "Build recorder: a system to capture detailed information"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/sbom_contents_discussion.webm",
    "title": "Discussion on SBOM contents"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/sbom_fusa.webm",
    "title": "Using SPDX for functional safety"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/sbom_reuse.webm",
    "title": "REUSE\nThe gold standard of communicating licensing and copyright information"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/sbom_toolchain_yocto.webm",
    "title": "A complete compliance toolchain for Yocto projects\n(even very large ones, yes)"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/sbom_survey.webm",
    "title": "In SBOMs We Trust: How Accurate, Complete, and Actionable Are They?"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/sbom_key_ingredients.webm",
    "title": "The 7 key ingredients of a great SBOM\nEnsuring your SBOM includes enough data to be actionable"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/sbom_panel.webm",
    "title": "Panel discussion: SBOM content, usefulness, and caveats"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/sbom_qna.webm",
    "title": "General Q&A on SBOMs"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.136/sbom_end.webm",
    "title": "SBOM devroom closing"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/sds_lessons_learnt_glusterfs.webm",
    "title": "Lessons learnt managing and scaling 200TB glusterfs cluster @PhonePe"
  },
  {
    "href": "https://video.fosdem.org/2023/D.sds/sds_vhost_user_blk.webm",
    "title": "vhost-user-blk: a fast userspace block I/O interface"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/sds_ceph_openstack.webm",
    "title": "Present and future of Ceph integration with OpenStack and k8s"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/sds_sql_on_ceph.webm",
    "title": "SQL on Ceph\nAn introduction to the new libcephsqlite library."
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/sds_dynamic_load_change.webm",
    "title": "Dynamic load change in SDS systems\nHow to make well behaved SDS systems in an ever changing cluster"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/sds_s3gw.webm",
    "title": "s3gw: easy to use S3-compatible gateway for small and edge deployments"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/sds_ceph_rgw_zipper.webm",
    "title": "Ceph RGW and Zipper\nAlternative Storage Backends for S3 and Swift Object Storage"
  },
  {
    "href": "https://video.fosdem.org/2023/D.sds/sds_ceph_dashboard.webm",
    "title": "Operating Ceph from Ceph Dashboard\nPast, Present and Furture"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/sds_rook_ceph.webm",
    "title": "Intro to Ceph on Kubernetes using Rook\nRook Ceph in Kubernetes and the rook-ceph krew plugin"
  },
  {
    "href": "https://video.fosdem.org/2023/H.2214/sds_keda_object_store.webm",
    "title": "AMENDMENT Autoscaling with KEDA - Object Store Case Study"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/sovcloud_opening_remarks.webm",
    "title": "A Sovereign Cloud - Opening Remarks"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/sovcloud_how_we_created_a_documentation_framework_that_works_across_a_group_of_vendors.webm",
    "title": "How we created a Documentation Framework that works across a group of vendors in the sovereign cloud stack community"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/sovcloud_is_open_source_coming_back_to_your_cloud.webm",
    "title": "Is Open Source Coming back to your Cloud?"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/sovcloud_on_premise_data_centers_do_not_need_to_be_legacy.webm",
    "title": "On-premise data centers do not need to be legacy\nWe can and should learn from legacy on-premise data centers and the migration to the cloud to ensure the computing platform's future is bright"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/sovcloud_distributed_storage_in_the_cloud.webm",
    "title": "Distributed Storage in the Cloud"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/sovcloud_from_zero_to_hero_with_solid.webm",
    "title": "From Zero to Hero with Solid\nLessons learned making apps using the Solid Protocol"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/sovcloud_operate_first_community_cloud.webm",
    "title": "Operate First community cloud\nA blueprint for a sovereign cloud?"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/sovcloud_responsible_clouds_and_the_green_web_triangle.webm",
    "title": "Responsible Clouds and the Green Web Triangle\nHow to make the climate case for a diverse cloud ecosystem"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/sovcloud_the_co_operative_cloud.webm",
    "title": "The Co-operative Cloud\nPublic interest infrastructure"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/sovcloud_the_importance_of_collaborative_applications_for_european_digital_sovereignty.webm",
    "title": "The Importance of Collaborative Applications for European Digital Sovereignty\nProgress and challenges of alternatives facing the BigTechs"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/sovcloud_the_role_of_open_infrastructure_in_digital_sovereignty.webm",
    "title": "The role of Open Infrastructure in digital sovereignty"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/sovcloud_the_role_of_open_source_at_the_eu_technology_roadmap_for_a_european_sovereign_cloud.webm",
    "title": "The Role of Open Source at the EU Technology Roadmap for a European Sovereign Cloud"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/sovcloud_what_is_digital_sovereignty_and_how_can_oss_help_to_achieve_it.webm",
    "title": "What is Digital Sovereignty and how can OSS help to achieve it?\nDemystifying an important term that has become a buzzword"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/sovcloud_effective_management_of_kubernetes_resources_for_cluster_admins.webm",
    "title": "Effective management of Kubernetes resources for cluster admins"
  },
  {
    "href": "https://video.fosdem.org/2023/H.1301%20(Cornil)/sovcloud_closing_remarks.webm",
    "title": "Z Sovereign Cloud - Closing Remarks"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/welcome.webm",
    "title": "Welcome to Testing and Automation devroom"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/linux_kernel_functional_testing.webm",
    "title": "Linux Kernel Functional Testing\nA look at the infrastructure"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/growing_testing_lab.webm",
    "title": "Growing a lab for automated upstream testing: challenges and lessons learned"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/vegvisir.webm",
    "title": "Introducing Vegvisir: An automation framework for testing QUIC application logic\nWho said using QUIC was easy?"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/observability_opentelemetry.webm",
    "title": "Observability-driven development with OpenTelemetry\nUse traces to enrich your integration tests!"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/openqa_for_gnome.webm",
    "title": "Setting up OpenQA testing for GNOME"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/termie.webm",
    "title": "Console Automation with Termie\nPractical and fun automation for all your terminal sessions"
  },
  {
    "href": "https://video.fosdem.org/2023/UB4.132/mutation_testing.webm",
    "title": "Fear the mutants. Love the mutants."
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/translations_welcome_to_the_translations_devroom.webm",
    "title": "Welcome to the Translations DevRoom\nLet's have a great afternoon talking about translating FOSS projects!"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/translations_translate_all_the_things.webm",
    "title": "Translate All The Things!\nAn Introduction to LibreTranslate"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/translations_bringing_your_project_closer_to_users_translating_libre_with_weblate.webm",
    "title": "Bringing your project closer to users – translating libre with Weblate\nNews, features and plans of the project"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/translations_20_years_with_gettext.webm",
    "title": "20 years with Gettext\nExperiences from the PostgreSQL project"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/translations_building_an_atractive_way_in_an_old_infra_for_new_translators.webm",
    "title": "Building an atractive way in an old infra for new translators"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/translations_managing_kdes_translation_project.webm",
    "title": "Managing KDE's translation project\nAre we the biggest FLOSS translation project?"
  },
  {
    "href": "https://video.fosdem.org/2023/AW1.120/translations_translating_documentation_with_cloud_tools_and_scripts.webm",
    "title": "Translating documentation with cloud tools and scripts\nUsing cloud tools and scripts to translate, review and update documents"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/vai_fuzzing_device_models.webm",
    "title": "Fuzzing Device Models in Rust: Common Pitfalls"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/vai_openstack_still_needed.webm",
    "title": "Is OpenStack still needed in 2023?"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/vai_using_spdk.webm",
    "title": "Using SPDK with the Xen hypervisor"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/vai_okd_virtualization.webm",
    "title": "OKD Virtualization: what’s new, what’s next\nNew features on OKD Virtualization 4.11 and 4.12 and next challenges"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/vai_stateless_decoder_virt.webm",
    "title": "Stateless decoder virtualization using VirtIO Video and Rust\nHow this will be used on ChromeOS and more."
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/vai_blkhash_fast_disk.webm",
    "title": "blkhash - fast disk image checksums"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/vai_dear_admin_my_network.webm",
    "title": "Dear admin, where’s my network?\nOverview of (un)reliable methods for vNIC to network mapping with KubeVirt"
  },
  {
    "href": "https://video.fosdem.org/2023/K.3.201/vai_journey_supporting_vms.webm",
    "title": "A journey through supporting VMs with dedicated CPUs on Kubernetes"
  },
  {
    "href": "https://video.fosdem.org/2023/UB2.147/vis_users.webm",
    "title": "vis users meeting\nBoF for users of the vis editor"
  }
]

### all one page
gen_html = "<table>"
for file_dict in files:
    json_file_name = "files/" + os.path.basename(file_dict['href']) + '.json'
    summary_file_name = "files/" + os.path.basename(file_dict['href']) + '.summary.txt'
    vtt_file_name = "files/" + os.path.basename(file_dict['href']) + '.vtt'
    file_dict['summary'] = summary_file_name if os.path.exists(summary_file_name) else False
    file_dict['vtt'] = vtt_file_name if os.path.exists(vtt_file_name) else False
    try:
        js = json.load(open(json_file_name, 'r'))
    except Exception:
        continue
    gen_html += "<tr><td><b>" + file_dict['title'] + "</b></td></tr><tr><td>" + js['text'] + "</td></tr>"

gen_html += "</table>"

tpl = open('template.html', 'r').read()
out_html = tpl.replace("###", gen_html)

out_file = open('big.html', 'w')
out_file.write(out_html)


### links

gen_html = '''<a href="big.html">All text in one big file</a>
<br><a href="https://fosdem.org/2023/schedule/events/">FOSDEM 2023 Event Page</a>
<table>'''
for file_dict in files:
    json_file_name = "files/" + os.path.basename(file_dict['href']) + '.json'
    txt_file_name = "files/" + os.path.basename(file_dict['href']) + '.txt'
    docsrc = file_dict['href'].replace("https://video.fosdem.org/", "https://mirrors.dotsrc.org/fosdem/")
    try:
        js = json.load(open(json_file_name, 'r'))
    except Exception:
        continue

    summary = ''
    if file_dict['summary']:
        summary = f'<a href="{file_dict["summary"]}">Summary</a> '

    vtt = ''
    if file_dict['vtt']:
        vtt = f' <a href="{file_dict["vtt"]}">WebVTT</a>'
    gen_html += f'''<tr>
      <td>
      <b>{file_dict['title']}</b>
      </td>
      <td>
        {summary}<a href="{json_file_name}">JSON</a> <a href="{txt_file_name}">txt</a>{vtt}
        <a href="{file_dict['href']}">Video</a> <a href="{docsrc}">Mirror&nbsp;Vid</a>
      </td>
      </tr>'''

gen_html += "</table>"

tpl = open('template.html', 'r').read()
out_html = tpl.replace("###", gen_html)

out_file = open('links.html', 'w')
out_file.write(out_html)
