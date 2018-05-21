from argparse import (
    ArgumentParser,
    SUPPRESS
)


class WhatWafParser(ArgumentParser):

    def __init__(self):
        super(WhatWafParser, self).__init__()

    @staticmethod
    def cmd_parser():
        parser = ArgumentParser(prog="whatwaf.py", add_help=True, usage=(
            "./whatwaf.py -[u|l] VALUE|PATH -[p|-pl] PAYLOADS --[args]"
        ))

        mandatory = parser.add_argument_group("mandatory arguments",
                                              "arguments that have to be passed for the program to run")
        mandatory.add_argument("-u", "--url", dest="runSingleWebsite", metavar="URL",
                               help="Pass a single URL to detect the protection")
        mandatory.add_argument("-l", "--list", "-f", "--file", dest="runMultipleWebsites", metavar="PATH",
                               help="Pass a file containing URL's (one per line) to detect the protection")

        req_args = parser.add_argument_group("request arguments",
                                             "arguments that will control your requests")
        req_args.add_argument("--pa", dest="usePersonalAgent", metavar="USER-AGENT",
                              help="Provide your own personal agent to use it for the HTTP requests")
        req_args.add_argument("--ra", dest="useRandomAgent", action="store_true",
                              help="Use a random user-agent for the HTTP requests")
        req_args.add_argument("--proxy", dest="runBehindProxy", metavar="PROXY",
                              help="Provide a proxy to run behind in the format "
                                   "type://address:port (IE socks5://10.54.127.4:1080")
        req_args.add_argument("--tor", dest="runBehindTor", action="store_true",
                              help="Use Tor as the proxy to run behind, must have Tor installed")
        req_args.add_argument("-p", "--payloads", dest="providedPayloads", metavar="PAYLOADS",
                              help="Provide your own payloads separated by a comma IE AND 1=1,AND 2=2")
        req_args.add_argument("--pl", dest="payloadList", metavar="PAYLOAD-LIST-PATH",
                              help="Provide a file containing a list of payloads 1 per line")
        req_args.add_argument("--force-ssl", dest="forceSSL", action="store_true",
                              help="Force the assignment of HTTPS instead of HTTP while processing")
        req_args.add_argument("--check-tor", dest="checkTorConnection", action="store_true",
                              help="Check your Tor connection")

        encoding_opts = parser.add_argument_group("encoding options",
                                                  "arguments that control the encoding of payloads")
        encoding_opts.add_argument("-e", "--encode", dest="encodePayload", nargs=2, metavar=("PAYLOAD", "TAMPER-SCRIPT-LOAD-PATH"),
                                   help="Encode a provided payload using a provided tamper script")
        encoding_opts.add_argument("-el", "--encode-list", dest="encodePayloadList", nargs=2, metavar=("PATH", "TAMPER-SCRIPT-LOAD-PATH"),
                                   help="Encode a file containing payloads (one per line) "
                                        "by passing the path and load path")

        output_opts = parser.add_argument_group("output options",
                                                "arguments that control how WhatWaf handles output")
        output_opts.add_argument("-F", "--format", action="store_true", dest="formatOutput",
                                 help="Format the output into a dict and display it")
        output_opts.add_argument("-J", "--json", action="store_true", dest="sendToJSON",
                                 help="Send the output to a JSON file")
        output_opts.add_argument("-Y", "--yaml", action="store_true", dest="sendToYAML",
                                 help="Send the output to a YAML file")
        output_opts.add_argument("-C", "--csv", action="store_true", dest="sendToCSV",
                                 help="Send the output to a CSV file")
        output_opts.add_argument("--fingerprint", action="store_true", dest="saveFingerprints",
                                 help="Save all fingerprints for further investigation")
        output_opts.add_argument("--tamper-int", metavar="INT", dest="amountOfTampersToDisplay", type=int,
                                 help="Control the amount of tampers that are displayed (default is 5)")

        misc = parser.add_argument_group("misc arguments",
                                         "arguments that don't fit in any other category")
        misc.add_argument("--verbose", dest="runInVerbose", action="store_true",
                          help="Run in verbose mode (more output)")
        misc.add_argument("--hide", dest="hideBanner", action="store_true",
                          help="Hide the banner during the run")
        misc.add_argument("--update", dest="updateWhatWaf", action="store_true",
                          help="Update WhatWaf to the newest development version")
        misc.add_argument("--save", dest="saveEncodedPayloads", metavar="FILENAME",
                          help="Save the encoded payloads into a file")
        misc.add_argument("--skip", dest="skipBypassChecks", action="store_true",
                          help="Skip checking for bypasses and just identify the firewall")
        misc.add_argument("--verify-num", dest="verifyNumber", metavar="INT", type=int,
                          help="Change the default amount (5) to verify if there really is not a WAF present")
        misc.add_argument("--tamper-dir", dest="tamperDir", metavar="FULL-PATH-TO-DIRECTORY",
                          help="Use only the tampers in the specified directory")

        hidden = parser.add_argument_group()
        hidden.add_argument("--clean", action="store_true", dest="cleanHomeFolder", help=SUPPRESS)

        opts = parser.parse_args()

        return opts

