from webpype.client import WebPypeClient

if __name__ == '__main__':
    webpipe = WebPypeClient()
    webpipe.print_options("http://status-code-retriever.herokuapp.com")
