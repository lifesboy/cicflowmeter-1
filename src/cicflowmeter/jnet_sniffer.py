import os

from cicflowmeter.util.logger import log
from scapy.sendrecv import AsyncSniffer


class JnetSniffer(AsyncSniffer):

    def _run(self,
             input_file=None,
             output_file=None,
             **karg  # type: Any
             ):
        # type: (...) -> None
        self.running = True

        # Start main thread
        try:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            cmd = f"{dir_path}/bin/convert_pcap_csv.sh {input_file} {output_file}"

            log.info('JnetSniffer: cmd=%s', cmd)
            self.results = os.system(cmd)
            log.info('JnetSniffer: results=%s', self.results)
        except Exception:
            pass

        self.running = False
