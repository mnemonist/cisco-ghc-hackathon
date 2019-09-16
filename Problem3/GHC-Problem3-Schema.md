# Description

This page describes the schema of the `flow` json output

# Example

```json
{
  "FlowTable": [
    {
      "Flow": {
        "component-A": {
          "ip": "169.254.59.75",
          "mac": "34:17:eb:d1:c5:ac",
          "port": 60014
        },
        "component-B": {
          "ip": "255.255.255.255",
          "mac": "ff:ff:ff:ff:ff:ff",
          "port": 3956
        },
        "ethernettype": "IPv4",
        "id": "685aca76-7615-53fe-84f5-919602632e27",
        "layer4": "UDP"
      },
      "FlowInfo": {
        "firstseen": "2015-07-09T16:24:30.605706+02:00",
        "lastseen": "2015-07-09T16:24:30.605706+02:00",
        "properties": [
          {
            "Source": "A",
            "Time": "2015-07-09T16:24:30.605706+02:00",
            "ipv4-ttl": 128
          }
        ],
        "properties_protocols": [
          "ipv4"
        ],
        "server": "Undetermined",
        "stats": [
          {
            "Direction": "A→B",
            "l2-bytes": 60,
            "l7-bytes": 16,
            "packets": 1
          }
        ]
      }
    },
  ],
  "Frame": {
    "Begin": "2015-07-09T14:15:35.250214+02:00",
    "End": "2015-07-09T16:28:17.826661+02:00"
  }
}
```

# Schema

The JSON is a representation of the traffic seen during a period of time and is composed of 2 elements:
- A FlowTable which is an array of FlowTrackerEntry items
- A Frame object which describes the time frame of the traffic analyzed

## FlowTable

FlowTable is mandatory and contains an array of FlowTrackerEntry objects

### FlowTrackerEntry

A FlowTrackerEntry object contains 2 mandatory elements:
- a Flow object
- a FlowInfo object

#### Flow

A Flow object represents a set of packets for a communication between two endpoints on the basis of their data, network, transport and application properties.

Strictly speaking, a flow is uniquely characterized by its endpoints' properties (MAC, IP, port and subAddr) through a function $`id ↦ f(a, b, c, d, e, f, g, h)`$ where $`f(macA, macB, ipA, ipB, portA, portB, subAddrA, subAddrB) = f(macB, macA, ipB, ipA, portB, portA, subAddrA, subAddrB)`$.

Flow attributes:

- component-A - mandatory - an object representing one of the flow's endpoint - Component
- component-B - mandatory - an object representing the other endpoint - Component
- ethertype - mandatory - Ethertype - integer
- layer4 - optionnal - last layer decoded - string
- vlanid - optionnal - VLAN ID - integer
- id - mandatory - unique flow ID - string

##### Component

- mac - mandatory - MAC address of the component - string
- ip - optionnal - IP address of the component - string
- port - optionnal - TCP port if the flow contains TCP - string
- subaddr - optionnal - rack number in the case of the ENIP/COTP protocol - string

#### FlowInfo

- firstseen - mandatory - First time we saw the not expired flow (a flow is considered expired if not seen 1 minute after the lastseen) - Timestamp with nano precision RFC3339
- lastseen - mandatory - last packet seen before expiration - Timestamp
- properties - mandatory - list of Property object - []Property
- properties_protocols - mandatory - list of seen protocols in the flow - []string
- stats - mandatory - packet statistics per direction - []FlowInfoStats
- server - mandatory - component role in the context of the identified protocol - string (3 possible values: "Undetermined", "A", "B")

##### properties

Data and metadata about the packet traffic

Source - mandatory - Component emitter of the packet - string ("A" or "B")
Time - mandatory - Time when seen - Timestamp
+ list of protocol attributes that are successfully extracted

##### properties_protocols

A list of protocols seen in the context of the flow

##### stats

Statistics about packets seen in each direction

direction - mandatory - Direction - string ("A->B" or "B->A")
l2-bytes - mandatory - number of bytes seen at the layer 2 - integer
l7-bytes - mandatory - estimation of bytes seen at the last decoded layer - integer
packets - mandatory - number of packets seen - integer