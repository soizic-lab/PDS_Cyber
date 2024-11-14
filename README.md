# Implementing Artifacts into the SPHERE RI

This file aimed at giving a more detailed insight at the proposed "ready-to-port" artifacts. All of these artifacts will be ported as Jupyter notebook files and come in a folder (Artifact 1,2,3,4 or 5 ) containing the topology model they require. 

## "Ready to port" artifacts

### Artifact 1 

**<ins>Paper</ins> :** [PRAC : Round-Efficient 3-Party MPC for Dynamic Data Structures](https://eprint.iacr.org/2023/1897.pdf)

Artifact 1 is from [PoPETs/PETS](https://petsymposium.org/cfp24.php) 2024 and the repository used to reproduce this artifact is the following : [https://git-crysp.uwaterloo.ca/iang/prac]

This artifact was created by Sajin Sasy (University of Waterloo, Waterloo, ON, Canada, ssasy@uwaterloo.ca), Adithya Vadapalli (IIT Kanpur, Kanpur, Uttar Pradesh, India, avadapalli@cse.iitk.ac.in) and Ian Goldberg (University of Waterloo, Waterloo, ON, Canada, iang@uwaterloo.ca).

PRAC is a 3-party MPC framework and enables efficient random-access data structures with optimized communication. Enhanced protocols for binary search, heaps, and AVL trees reduce rounds and bandwidth, showing significant performance gains in real-world network settings.

### Artifact 2 

**<ins>Paper</ins> :** [Differentially Private Resource Allocation](https://bpb-us-e2.wpmucdn.com/faculty.sites.uci.edu/dist/5/764/files/2023/11/acsac23.pdf)

Artifact 2 is from [ACSAC 2023](https://www.acsac.org/2023/program/artifacts/) and the repository used to reproduce this artifact is the following : [https://github.com/dpra-dp/dpra]

This artifact was created by Joann Qiongna Chen (University of California, Irvine, CA, USA), Tianhao Wang (University of Virginia, Charlottesville, VA), Zhikun Zhang(CISPA Helmholtz Center for Information Security,Saarbrücken, Stanford University), Yang Zhang (CISPA Helmholtz Center for Information Security, Saarbrücken), Somesh Jha (University of Wisconsin, Madison, WI, USA) and Zhou Li (University of California, Irvine, CA, USA).

Recent research highlights that metadata-private systems like MPM are vulnerable to side-channel attacks through resource allocation, compromising user privacy. Four new noise mechanisms refine differential privacy (DP) techniques to better model attacker uncertainty, achieving improved privacy-utility tradeoffs over previous methods.

### Artifact 3 

**<ins>Paper</ins> :** [On the Feasibility of Cross-Language Detection of Malicious Packages in npm and PyPI](https://dl.acm.org/doi/fullHtml/10.1145/3627106.3627138)

Artifact 3 is from ACSAC 2023 and the repository used to reproduce this artifact is the following : [https://github.com/SAP-samples/cross-language-detection-artifacts]

This artifact was created by Piergiorgio Ladisa (SAP Security Research, Université de Rennes, INRIA, IRISA, France, piergiorgio.ladisa@sap.com),  Serena Elisa Ponta (SAP Security Research, France, serena.ponta@sap.com),  Nicola Ronzoni (SAP Security Research, France, nicola.ronzoni@studio.unibo.it), Matias Martinez (Universitat Politècnica de Catalunya-BarcelonaTech, Spain, matias.sebastian.martinez@gmail.com) and  Olivier Barais (Université de Rennes, Inria, CNRS, IRISA, France, olivier.barais@irisa.fr).

Open-source software supply chains, heavily dependent on public repositories like npm and PyPI, are increasingly targeted by attackers spreading malware through malicious packages. A new approach, using language-independent features to detect malware across ecosystems, has identified 58 previously unknown malicious packages, enhancing security for npm and PyPI.


### Artifact 4 

**<ins>Paper</ins> :** [Hades: Practical Decentralized Identity with Full Accountability and Fine-grained Sybil-resistance](https://dl.acm.org/doi/pdf/10.1145/3627106.3627110)

Artifact 4 is from ACSAC 2023 and the repository used to reproduce this artifact is the following : [https://github.com/didnet/zxDID]

This artifact was created by Ke Wang (Beijing Univeristy, wangk@pku.edu.cn), Jianbo Gao (Beijing Univeristy), Qiao Wang (Beijing University), Jiashuo Zhang (Beijing University, China), Yue Li (Beijing University, China), Zhi Guan (Beijing University, China), and Zhong Chen (Beijing University, China).

Hades, a novel decentralized identity (DID) system, addresses privacy, accountability, and Sybil resistance in decentralized applications (Dapps). It supports auditability, traceability, and revocation with minimal gas costs on the Ethereum Virtual Machine (EVM), outperforming previous systems and enabling efficient fair NFT distributions.

### Artifact 5

**<ins>Paper</ins> :** [Poisoning Network Flow Classifiers](https://dl.acm.org/doi/pdf/10.1145/3627106.3627123)

Artifact 5 is from ACSAC 2023 and the repository used to reproduce this artifact is the following : [https://github.com/ClonedOne/poisoning_network_flow_classifiers]
Two notebooks are available for this artifact, the first one enables the display of graphs only, the second one enables the display of both graphs and tables except for some figures where it's specified. 

This artifact was created by Giorgio Severi (Northeastern University, Boston, MA, USA), Simona Boboila (Northeastern University, Boston, MA, USA), Alina Oprea (Northeastern University, Boston, MA, USA), John Holodnak (MIT Lincoln Lab,Lexington, MA, USA), Kendra Kratkiewicz (MIT Lincoln Lab, Lexington, MA, USA) and  Jason Matterer (STR, Woburn, MA, USA).

This artifact enables performing backdoor poisoning attacks against network flow classifiers. The manipulation of aggregated traffic flow features, rather than packet-level content, is the focus of this artifact, with emphasis on statistical features derived from connection metadata extracted using Zeek.

## Unresolved artifacts

### Fuzzbench-triereme

**<ins>Paper</ins> :** [Triereme : Speeding up hybrid fuzzing through efficient query scheduling](https://goto.ucsd.edu/~gleissen/papers/triereme.pdf)

See PDF for explanation about what was done on the node.

The repository for this artifact is the following : [https://github.com/vusec/fuzzbench-triereme]

This artifact was created by Elia Geretto (Vrije Universiteit Amsterdam, Amsterdam, the Netherlands, e.geretto@vu.nl), Julius Hohnerlein (Vrije Universiteit Amsterdam, Amsterdam, the Netherlands, julius.hohnerlein@posteo.de), Cristiano Giuffrida (Vrije Universiteit Amsterdam, Amsterdam, the Netherlands, giuffrida@cs.vu.nl), Herbert Bos (Vrije Universiteit Amsterdam, Amsterdam, the Netherlands, herbertb@cs.vu.nl), Erik van der Kouwe (Vrije Universiteit Amsterdam, Amsterdam, the Netherlands, vdkouwe@cs.vu.nl) and Klaus v. Gleissenthall (Vrije Universiteit Amsterdam, Amsterdam, the Netherlands, k.freiherrvongleissenthal@vu.nl).

Hybrid fuzzing, combining fuzzing and concolic execution, has struggled to meet expectations due to high overhead, particularly from time spent in the SMT solver. Triereme addresses this by using a trie data structure to optimize query scheduling and caching, resulting in a 6.1x speedup in concolic executions and improved coverage in 79% of benchmarks.

### Detection of Anomalies in Electric Vehicle Charging Sessions web

**<ins>Paper</ins> :** [Detection of Anomalies in Electric Vehicle Charging Sessions](https://dl.acm.org/doi/pdf/10.1145/3627106.3627127)

Code issue

The repository for this artifact is the following : [https://code.fbi.h-da.de/seacop/ev-charging-ids-data-sets/]

This artifact was created by Dustin Kern (Darmstadt University of Applied, Sciences, Darmstadt, Germany, dustin.kern@h-da.de), Christoph Krauß (Darmstadt University of Applied, Sciences, Darmstadt, Germany, christoph.krauss@h-da.de) and Matthias Hollick (Technical University of Darmstadt, Darmstadt, Germany, mhollick@seemoo.tu-darmstadt.de).

Electric Vehicle (EV) charging systems, with their cyber-physical components and communication protocols, are vulnerable to security incidents that could lead to serious threats. A hybrid Intrusion Detection System (IDS) method is proposed, combining regression-based charging session forecasting and anomaly detection, which significantly improves detection performance, reduces false alarms, and generalizes well to new attacks.


 
