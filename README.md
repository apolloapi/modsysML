# modsys: model management tool

[![python](https://img.shields.io/pypi/pyversions/3)](https://www.python.org/downloads/)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/modsysML/modsys/pre-commit.yml)
![Release](https://img.shields.io/github/v/release/modsysML/modsys)

<!-- <div align="center">

![HowItWorks](https://uploads-ssl.webflow.com/640ca38ad086fde245b76c9d/645e8d8ad611b140135e11bb_GraphicOne.png)

</div> -->

<div align="center">
ModsysML is an upstream open-source validation framework for testing, automating and data analytics.
</div>

<p align="center">
    <br />
    <a href="#" rel="dofollow"><strong>Docs [Coming soon]»</strong></a>
    <br />

  <br/>
    <a href="https://www.apolloapi.io/">Join the waitlist</a>
    ·
    <a href="https://github.com/modsysML/modsys/issues">Report Bug</a>
    ·
    <a href="https://discord.gg/ZUH7f7AzUY">Community Discord</a>
</p>

## Why ModsysML?

Before modsys, running proactive intelligence & insights through testing data quality and automating workloads was time-consuming, with modsys, you can simplify, accelerate and backtest the entire process. This makes it easier to train classifiers, handle real-time changes and make data driven decisions.

## 🚀 Interesting, how can I try it?

Lets install the SDK first...

```bash
pip install modsys
```

## Regression tests vs Automated pipelines

`modsys` helps you tune LLM prompts systematically across many relevant test cases. By evaluating and comparing LLM outputs to build decision making workflows. Users can test prompt quality and catch regressions faster.

### Evaluating prompt quality

**With Modsys python library and CLI toolkit, you can:**

- **Detecting real-time changes** in your data
- Automating tasks against **image, video, audio or text**
- Simplifying the process of **back-testing quality** for your AI models
- Making sure your integration is robust, so you **never again have to worry about stuck/stale data or false-positives**
- **Test multiple prompts** against predefined test cases
- **Evaluate quality and catch regressions** by comparing LLM outputs side-by-side
- **Speed up evaluations** with caching and concurrent tests
- **Flag bad outputs automatically** by setting "expectations"
- Use as a **command line tool, or integrate into your workflow with our library**
- **Use any** AI provider, API or database under one API

`modsys` produces table views that allow you to quickly review prompt outputs across many inputs. The goal: tune prompts systematically across all relevant test cases, instead of testing prompts by trial and error.

#### Usage (command line)

_Support for user interface coming soon_

**It works on the command line, you can output to [`json`, `csv`, `yaml`]:**

![Prompt eval](https://github.com/apolloapi/apolloapi/assets/72639210/c65b4565-5d17-4b32-971c-d4a51d9d137e)

To get started, run the following command:

```
modsys init
```

This will create some templates in your current directory: `prompts.txt`, `vars.csv`, and `config.json`.

After editing the prompts and variables to your desired state, `modsys` command to kick off an prompt evaluation test:

```
modsys -p ./prompts.txt -v ./vars.csv -r openai:completion
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

### Examples

#### Prompt quality

In this example, we evaluate whether adding adjectives to the personality of an chat bot affects the responses:

```bash
modsys -p prompts.txt -v vars.csv -r openai:gpt-3.5-turbo
```

![Prompt eval](https://uploads-ssl.webflow.com/640ca38ad086fde245b76c9d/647411b456031b5145019909_Screenshot%202023-05-28%20at%2010.44.48%20PM.png)

This command will evaluate the prompts in `prompts.txt`, substituing the variable values from `vars.csv`, and output results in your terminal.

Have a look at the setup and full output in another format:

```
modsys -p prompts.txt -v vars.csv -r openai:gpt-3.5-turbo -o output.json
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
modsys -p prompts.txt -r hiveai:hate google:safety -o output.json
```

#### Configuration

- **Setting up an model test**: Learn more about how to set up prompt files, vars file, output, etc.

### Building Automated Pipelines in the User Interface or Programmatically

![image](https://github.com/apolloapi/apolloapi/assets/72639210/602234c2-f855-4514-8188-505c0d6c39c1)

Let's setup your first Integration!

It will pull from your local database (and keep it in sync).

```python
# import the package
from modsys.client import Modsys

# sync data from your database instance
# (we support supabase at the current moment or postgresql via uri format)
Modsys.connect("postgres://username:password@hostname:port/database_name")

# If you want to test out operation on your external connection
Modsys.fetch_tables()
Modsys.query("desc", "table", "column")
```

...and create a workflow with a simple command:

```python
# import the package
from modsys.client import Modsys

# Use any provider
Modsys.use("google_perspective:<model name>", google_perspective_api_key="YOUR_API_TOKEN_HERE")

# An option for image detection, connect to sightengine provider or other image service first
Modsys.detectImage('https://example.com/some-endpoint') # Image Analysis/OCR

# Lets check to see if a phrase contains threats
Modsys.detectText(prompt="Phrase1", content_id="content-id", community_id="user-id")
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
Modsys.rule('Phrase1', '>=', '0.8')

Modsys.detectImage('Image1', 'contains', 'VERY_LIKELY') # Image Analysis/OCR
Modsys.detectSpeech('Audio1', 'contains', 'UNLIKELY') # Audio Processing
Modsys.detectVideo('Video1', 'contains', 'POSSIBLE') # Video Analysis
Modsys.detectText('Phrase1', 'contains', 'UNKNOWN') # Text Analysis
Modsys.test('prompt', 'expected_output') # ML Validation
```

That's all it takes!

In practice, you probably want to use one of our native SDKs to interact with different AI providers or use our custom browser client so you dont have to write code. If so, sign up for the downstream [Apollo ModsysML Console](https://use.apolloapi.io/admin/)!

##### Cool, what can I build with it?

- Modsys can help you **quickly automate tasks** for model management, performance, labeling, object detection and more.
- Teams can use Modsys to **build native in-app connections** related to active response, content moderation, risk management, fraud detection, etc.
- Some **automate their personal lives** with Modsys by integrating against discord communities or their personal lives

## Development

Contributions are welcome! Please feel free to submit a pull request or open an issue.

### 📦 pre-commit config

As an open source project, Modsys welcomes contributions from the community at large. This isn’t an exhaustive reference and is a living document subject to change as needed when the project formalizes any practice or pattern.

Clone the repo and start Modsys locally...

```bash
git clone https://github.com/modsysML/modsys.git
cd modsys && python3 -m venv env && source env/bin/activate && pip install -r requirements.txt
```

- After installing system dependencies be sure to install pre-commit for lint checks

```bash
pip install pre-commit

pre-commit install

pre-commit run --all-files
```

Modsys uses commit messages for automated generation of project changelog. For every pull request we request contributors to be compliant with the following commit message notation.

```
<type>: <summary>

<body>
```

Accepted `<type>` values:

- new = newly implemented user-facing features
- chg = changes in existing user-facing features
- fix = user-facing bugfixes
- oth = other changes which users should know about
- dev = any developer-facing changes, regardless of new/chg/fix status

##### Summary (The first line)

The first line should not be longer than 75 characters, the second line is always blank and other lines should be wrapped at 80 characters.

## 🔍 Neat, I would like to learn more

⭐ Follow our development by starring us here on GitHub ⭐

- Share feedback or chat with us on the [Discord community](https://discord.gg/ZUH7f7AzUY)

## AI Providers

We support OpenAI as well as a number of models. It's also possible to set up your own custom AI provider.
