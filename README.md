# twikirefs

A simple tool to retrieve the current references runs from the [Tracker twiki page](https://twiki.cern.ch/twiki/bin/view/CMS/TrackerOfflineReferenceRuns).

## Installation

```bash
pip install git+https://github.com/ptrstn/twikirefs
``` 

## Prerequisites

Setup your CERN Grid User Certificate as instructed in the cernrequests package:

- https://github.com/ptrstn/cernrequests#prerequisites

## Usage

```bash
twikirefs
```

Output:

```
Twiki Reference Runs

Acquiring CERN SSO Cookie for https://twiki.cern.ch/twiki/bin/view/CMS/TrackerOfflineReferenceRuns...
Retrieving Twiki page...
Parsing HTML site...
Done.

== Heavy Ion Collisions 2018 ==
['326384', '326528', '326502', '326722', '326855', '327237']

== pp Collisions 2018 ==
['323940', '323940', '321755', '321755', '321067', '321067', '318953', '318953', '317435', '317435', '317434', '317434', '316505', '316505', '316457', '316457', '315713', '315705', '315322', '315189', '314811', '314575']

== Cosmics 2018 ==
['326486', '323586', '321104', '318163', '318112', '317464', '315777', '314768', '313130', '314811', '313105', '312727', '312654', '312220', '312001', '311790', '311532', '311518', '311450', '311024', '309247']

Saved reference runs in 'twiki_reference_runs.json'
```

## References

- https://twiki.cern.ch/twiki/bin/view/CMS/TrackerOfflineReferenceRuns