##### Examples

    ajvb:$ python print_options.py

    {
      "name": "HTTP Status Code Retriever",
      "url": "http://status-code-retriever.herokuapp.com",
      "description": "Visits the given URL and returns the HTTP status code.",
      "inputs": [
        {
          "name": "url",
          "type": "String",
          "description": "URL to be visited."
        }
      ],
      "outputs": [
        {
          "name": "status_code",
          "type": "Number",
          "description": "HTTP status code returned by given URL."
        }
      ]
    }

