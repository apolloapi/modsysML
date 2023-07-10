# Google

Your connection to any AI Provider or third party app is called a connector. You can find information on setting up google perspective [here](https://developers.google.com/codelabs/setup-perspective-api#0)

`apollo-sdk` supports a wide range of models out of the box. To use a custom AI provider, create a custom module open an issue and we'll put some code together for you.

### Notes

To use the Google Comment Analyzer API, set the `PERSPECTIVE_API_KEY` environment variable or pass the API key as an argument to the constructor.

Example:

```bash
export PERSPECTIVE_API_KEY=your_api_key_here
```

or

```python
from apollo.client import Apollo

Apollo.use("google_perspective:analyze", google_perspective_api_key="token")
```

Other Perspective-related environment variables are supported:

- `PERSPECTIVE_CACHE_OUTPUT` - You can persist settings for the doNotScore configuration for the API. This setting is responsible for improving the model output over time for the dataset. The default value is True. Users can set the "doNotStore" flag to ensure that all submitted comments are automatically deleted after scores are returned. To set this, you need to override the cache variable in the same way as overriding existing class variables or set the state using PERSPECTIVE_CACHE_OUTPUT.

The Google provider supports the following model formats:

- `google_perspective:analyze` - defaults to analyzer
- `google_perspective:suggest` - defaults to suggestor
- `google_perspective:<model name>` - uses a specific model name (mapped automatically to chat or completion endpoint)

#### Google Perspective Connector

The Google Perspective LLM (Language Model) is a tool that enhances LLM output and can be coupled with a Machine Learning validation tool. Users have the option to extend this open-source connector by implementing new attributes to return and more.

### Setting up your own API

To set up your own API, please follow the instructions provided in the [Google Perspective API setup guide](https://developers.google.com/codelabs/setup-perspective-api#4).

### GooglePerspectiveProvider Client

The GooglePerspectiveProvider is a class that allows you to interact with the Google Perspective API. Here are some important details about this provider:

- The `api_key` can be set using the environment variable `PERSPECTIVE_API_KEY`. It can also be overridden in code by directly setting the `api_key_val` or more specifically through specifying a `secret` since it's a class variable.
- An array of languages to support can be set. The default language is `en`. [Google Perspective API language guide](https://developers.perspectiveapi.com/s/about-the-api-attributes-and-languages?language=en_US)
- If the API token is not set via the environment variable (default behavior), you will need to specify the token using the `secret` parameter.
- There are two model types available: `suggest` and `analyze`.
- You can set your model name during the connection using the use method and specifying `google_perspective:<model type>`.
- You can persist settings for the `doNotScore` configuration for the API. This setting is responsible for improving the model output over time for the dataset. The default value is `True`. Users can set the `"doNotStore"` flag to ensure that all submitted comments are automatically deleted after scores are returned. To set this, you need to override the cache variable in the same way as overriding existing class variables or set the state using `PERSPECTIVE_CACHE_OUTPUT`.
- To use the Google provider, you need to set the following parameters:

```python
Apollo.use("google_perspective:analyze", google_perspective_api_key=<API KEY(optional)>)
```

### Attributes tracked using Perspective

The following attributes are tracked using Perspective:

- `TOXICITY`: A rude, disrespectful, or unreasonable comment that is likely to make people leave a discussion.
- `SEVERE_TOXICITY`: A very hateful, aggressive, disrespectful comment or otherwise very likely to make a user leave a discussion or give up on sharing their perspective. This attribute is much less sensitive to more mild forms of toxicity, such as comments that include positive uses of curse words.
- `INSULT`: Insulting, inflammatory, or negative comment towards a person or a group of people.
- `THREAT`: Describes an intention to inflict pain, injury, or violence against an individual or group.
- `SEXUALLY_EXPLICIT`: Contains references to sexual acts, body parts, or other lewd content.
- `SPAM: Irrelevant and unsolicited commercial content.

Example Request and Response

Here is an example of the request and response when using the `Analyze` model:
\*Suggest model coming soon.

- Request:

```json
{
  "comment": {
    "text": "string"
  },
  "requestedAttributes": {
    "<ATTR[toxicity, identity attack, threat, sexuality_explicit, flirtation, spam]>": {}
  },
  "languages": ["en"],
  "doNotStore": false,
  "clientToken": "content-id",
  "communityId": "username"
}
```

Response:

```json
{
  "attributeScores": {
    "string": {
      "summaryScore": {
        "value": 0.5,
        "type": "string"
      },
      "spanScores": [
        {
          "begin": 0,
          "end": 10,
          "score": {
            "value": 0.5,
            "type": "string"
          }
        }
      ]
    }
  },
  "languages": ["string"],
  "clientToken": "string"
}
```

The response object contains the following information:

- `clientToken` (optional): An opaque token that is echoed back in the response.
- `communityId` (optional): An opaque identifier associating this comment with a particular community within your platform. If set, this field allows us to differentiate comments from different communities, as each community may have different norms.
