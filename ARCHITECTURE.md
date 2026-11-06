# HomeHarvest Architecture Overview

This repository is a Python experimentation and automation workspace: it combines scripts for desktop automation, web scraping, chatbot interactions, game logic, data processing, and reporting. The architecture below reflects that broad set of capabilities.

```mermaid
flowchart LR
    User[User / Developer] --> Entry[Python Entry Points\nmain.py, scripts, notebooks]

    Entry --> Apps[Application Scripts\nGames, Chatbots, Alarm, Receipt, UI tools]
    Entry --> Automation[Automation Layer\nPyAutoGUI, Selenium, OS tools]
    Entry --> DataOps[Data & Analysis Layer\nCSV, JSON, scraping, finance, reports]

    Apps --> UI[Interactive User Experience\nCLI / GUI / local app flows]
    Automation --> Browser[Browser Automation\nSelenium / web interaction]
    Automation --> Desktop[Desktop Automation\nPyAutoGUI / system control]

    Browser --> Web[External Websites / APIs / Data Sources]
    Desktop --> OS[Operating System / Local Files / Screen]
    DataOps --> Scrapers[Web Scrapers\nnews, real-estate, stock, IMDb]
    DataOps --> Analysis[Python Processing\nparsing, transformation, analytics]

    Web --> DataStore[(Local Data Files\nCSV, PDF, JSON, logs)]
    Scrapers --> DataStore
    Analysis --> Reports[Reports / Notifications / Visual outputs]

    Reports --> User
    UI --> User

    subgraph Repo[HomeHarvest Repository]
        Entry
        Apps
        Automation
        DataOps
    end

    subgraph External[External World]
        Web
        OS
        Browser
        Desktop
    end
```

## Architectural Notes

- Entry points are a mix of standalone scripts and small app modules rather than a single monolithic application.
- The repository uses a layered approach:
  - User interaction layer
  - Automation layer
  - Data acquisition and processing layer
  - Output/reporting layer
- External dependencies include websites, browser automation, local system control, and local/generated files.
- The design is intentionally flexible and script-oriented, suitable for experimentation and learning rather than a production service architecture.

## Typical Components in the Repo

- Automation scripts: UI control, browser interaction, system operations
- Data scraping scripts: news, real estate, movies, stocks
- Utility apps: receipt generator, chatbot, alarm clock, todo list
- Data outputs: CSV, PDF, reports, generated logs
- Experimental tools: games, visualizers, and learning projects
