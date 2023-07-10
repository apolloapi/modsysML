---
sidebar_position: 0
---

# Getting Started

Before Apollo, testing model quality and automating workloads was time-consuming, with Apollo, you can simplify, accelerate and backtest the entire process. This makes it easier to train classifiers, handle real-time changes and make data driven decisions.

Lets install the SDK first...

```bash
pip install apollo-sdk
```

### Evaluating prompt quality

`apollo-sdk` produces table views that allow you to quickly review prompt outputs across many inputs. The goal: tune prompts systematically across all relevant test cases, instead of testing prompts by trial and error.

#### Usage (command line)

_Support for user interface coming soon_

**It works on the command line, you can output to [`json`, `csv`, `yaml`]:**

![Prompt eval](https://github.com/apolloapi/apolloapi/assets/72639210/c65b4565-5d17-4b32-971c-d4a51d9d137e)
To get started, run the following command:

```
apollo-sdk init
```

This will create some templates in your current directory: `prompts.txt`, `vars.csv`, and `config.json`.

After editing the prompts and variables to your desired state, `apollo-sdk` command to kick off an prompt evaluation test:

```
apollo-sdk -p ./prompts.txt -v ./vars.csv -r openai:completion
```

If you're looking to customize your usage, you have a wide set of parameters at your disposal. See the [Configuration docs](https://docs.apolloapi.io/docs/api/configuration_tests) for more detail:

| Option                                           | Description                                                                                                                                            |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `-p, --prompts <paths...>`                       | Paths to prompt files, directory, or glob                                                                                                              |
| `-r, --providers <name or path...>`              | One of: openai:chat, openai:completion, openai:model-name, hive:hate, google:safety, etc. See [AI Providers](https://docs.apolloapi.io/docs/providers) |
| `-o, --output <path>`                            | Path to output file (csv, json, yaml, html)                                                                                                            |
| `-v, --vars <path>`                              | Path to file with prompt variables (csv, json, yaml)                                                                                                   |
| `-c, --config <path>`                            | Path to configuration file. `config.json` is automatically loaded if present                                                                           |
| `-j, --max-concurrency <number>` _coming soon_   | Maximum number of concurrent API calls                                                                                                                 |
| `--table-cell-max-length <number>` _coming soon_ | Truncate console table cells to this length                                                                                                            |
| `--grader` _coming soon_                         | Provider that will grade outputs, if you are using                                                                                                     |

<!-- After running a test against your model output, you may optionally use the `view` command to open the web viewer:

```
apollo-sdk show
``` -->

### Examples

#### Prompt quality

In this example, we evaluate whether adding adjectives to the personality of an chat bot affects the responses:

```bash
apollo-sdk -p prompts.txt -v vars.csv -r openai:completion
```

![Prompt eval](https://uploads-ssl.webflow.com/640ca38ad086fde245b76c9d/647411b456031b5145019909_Screenshot%202023-05-28%20at%2010.44.48%20PM.png)

This command will evaluate the prompts in `prompts.txt`, substituing the variable values from `vars.csv`, and output results in your terminal.

Have a look at the setup and full output in another format:

```
apollo-sdk -p prompts.txt -v vars.csv -r openai:completion -o ./output.json
```

You can also output a nice **spreadsheet, JSON, or YAML** file:

```json
{
  "results": [
    {
      "prompt": {
        "raw": "Rephrase this in French: Hello world",
        "display": "Rephrase this in French: {{body}}"
      },
      "vars": {
        "body": "Hello world"
      },
      "response": {
        "output": "Bonjour le monde",
        "tokenUsage": {
          "total": 19,
          "prompt": 16,
          "completion": 3
        }
      }
    }
    // ...
  ],
  "stats": {
    "successes": 4,
    "failures": 0,
    "tokenUsage": {
      "total": 120,
      "prompt": 72,
      "completion": 48
    }
  }
}
```

Here's an example of a side-by-side comparison of multiple prompts and inputs:

#### Model quality

You can evaluate the difference between safety outputs for a specific context:

_Model quality tests & python package for model testing is a beta feature at the moment, open an issue and tag us to setup_

```bash
apollo-sdk -p prompts.txt -r hiveai:hate google:safety -o output.json
```

<!-- ## Usage (python package)

You can also use `apollo` client as a library in your project by importing the `test` function. The function takes the following parameters:

- `providers`: a list of provider strings or `AIProvider` objects as a connector, or just a single string or `Connector` (connectors = providers).
- `options`: the prompts and variables you want to test:

  ```python
  {
    prompts: [str];
    vars: [];
  }
  ```

### Example

`apollo-sdk` exports a `test` function that you can use to run prompt evaluations.

```
``` -->

#### Configuration

- **[Setting up an model test](https://docs.apolloapi.io)**: Learn more about how to set up prompt files, vars file, output, etc.
<!-- - **[Configuring test cases]()**: Learn more about how to configure expected outputs and test assertions. -->

### Building Automated Pipelines

##### [View full documentation »](https://docs.apolloapi.io/)

Let's setup your first Integration!

It will pull from your local database (and keep it in sync).

```python
# import the package
from apollo.client import Apollo

# sync data from your database instance
# (we support supabase at the current moment or postgresql via uri format)
Apollo.connect("postgres://username:password@hostname:port/database_name")

# If you want to test out operation on your external connection
Apollo.fetch_tables()
Apollo.query("desc", "table", "column")
```

...and create a workflow with a simple command:

_Note: you can use our sandbox api and skip providing a token or obtain a Auth token [here](https://docs.apolloapi.io/docs/api/authentication), sign up today on our [Site](https://use.apolloapi.io/admin/)_

```python
# import the package
from apollo.client import Apollo

# Use any provider
Apollo.use("google_perspective:<model name>", secret="YOUR_API_TOKEN_HERE")

# Lets check to see if a phrase contains threats
Apollo.detectText(prompt="Phrase1", content_id="content-id", community_id="user-id")
```

**Example response**:

```json
{
  "attributeScores": {
    "THREAT": {
      "spanScores": [
        {
          "begin": 0,
          "end": 12,
          "score": { "value": 0.008090926, "type": "PROBABILITY" }
        }
      ],
      "summaryScore": { "value": 0.008090926, "type": "PROBABILITY" }
    },
    "INSULT": {
      "spanScores": [
        {
          "begin": 0,
          "end": 12,
          "score": { "value": 0.008804884, "type": "PROBABILITY" }
        }
      ],
      "summaryScore": { "value": 0.008804884, "type": "PROBABILITY" }
    },
    "SPAM" // ...
  },
  "languages": ["en"],
  "clientToken": "content_123",
  "detectedLanguages": ["en", "fil"]
}
```

_Experimental inputs_:

```python
# Create custom rules which creates a task!
Apollo.rule('Phrase1', '>=', '0.8')

# https://docs.apolloapi.io/docs/features
Apollo.detectImage('Image1', 'contains', 'VERY_LIKELY') # Image Analysis/OCR
Apollo.detectSpeech('Audio1', 'contains', 'UNLIKELY') # Audio Processing
Apollo.detectVideo('Video1', 'contains', 'POSSIBLE') # Video Analysis
Apollo.detectText('Phrase1', 'contains', 'UNKNOWN') # Text Analysis
Apollo.test('prompt', 'expected_output') # ML Validation
```

That's all it takes!

In practice, you probably want to use one of our native SDKs to interact with Apollo's API or use our custom browser client so you dont have to write code. If so, sign up at [Apollo API](https://use.apolloapi.io/admin/)!
