# PhishPlayer

Phish player is a Record & Replay tool that aims at
recording web interactions of an user with phishing websites
and replaying the steps. The purpose is for the tool to aid
forensic analysts to understand how the attack happened in the
first place.The attack is reconstructed by modifying chromium
telemetry tool that was developed by Chrome basically intended
to measure performance of websites. Since this reconstruction
provides an exact simulation of how the user interacted with the
phishing site, it provides a better insight in to the nuances of the
phishing community. If sufficient analysis was done on the data
collected , it may help detect the phishing sites in the initial stages
and necessary actions could be taken on blocking those sites.
