#
# Copyright 2018 Microsoft Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Requires Python 2.6+ and Openssl 1.0+
#


class RouteEntry(object):
    """
    Represents a single route. The destination, gateway, and mask members are hex representations of the IPv4 address in
    network byte order.
    """
    def __init__(self, interface, destination, gateway, mask, flags, metric):
        self.interface = interface
        self.destination = destination
        self.gateway = gateway
        self.mask = mask
        self.flags = int(flags, 16)
        self.metric = int(metric)

    @staticmethod
    def _net_hex_to_dotted_quad(value):
        if len(value) != 8:
            raise Exception("String to dotted quad conversion must be 8 characters")
        octets = []
        for idx in range(6, -2, -2):
            octets.append(str(int(value[idx:idx+2], 16)))
        return ".".join(octets)

    def destination_quad(self):
        return self._net_hex_to_dotted_quad(self.destination)

    def gateway_quad(self):
        return self._net_hex_to_dotted_quad(self.gateway)

    def mask_quad(self):
        return self._net_hex_to_dotted_quad(self.mask)

    def __str__(self):
        return "Iface: {0}\tDestination: {1}\tGateway: {2}\tMask: {3}\tFlags: {4}\tMetric: {5}" \
               .format(self.interface, self.destination_quad(), self.gateway_quad(), self.mask_quad(),
                       self.flags, self.metric)

    def __repr__(self):
        return 'RouteEntry("{0}", "{1}", "{2}", "{3}", "{4}", "{5}")'\
            .format(self.interface, self.destination, self.gateway, self.mask, self.flags, self.metric)