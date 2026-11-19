# PDF Password Auditing Lab

**John the Ripper · Johnny GUI · NetworkWalks Tools**

A concise, evidence-led record of two guided cybersecurity lab modules focused on password auditing of sample PDF documents.

## Project details

| Field | Details |
|---|---|
| Author | Mohit Dinesh Sonawane |
| Institution | Sandip Institute of Engineering and Management (SIEM) |
| Programme | Computer Engineering · Second Year |
| Completed | 19 November 2026 |
| Environment | Windows desktop and web browser |

## Modules

### 01 — John the Ripper and Johnny

The desktop workflow covers configuring John the Ripper through Johnny, extracting a PDF hash, loading the hash file, running an audit, and reviewing the displayed result.

**Tools:** [John the Ripper](https://www.openwall.com/john/) · [Johnny GUI](https://openwall.info/wiki/john/johnny/)

### 02 — NetworkWalks tools

The supplied Module 2 guide describes extracting a PDF hash with the NetworkWalks Hash Calculator and submitting it to the NetworkWalks Password Cracker.

**Tools:** [Hash Calculator](https://networkwalks.com/hash-calculator/) · [Password Cracker](https://networkwalks.com/password-cracker/) · [Project guide](https://networkwalks.com/project-task-lab-password-cracking-with-networkwalks-tools/)

> **Evidence note:** The supplied screenshots document the Johnny/JTR setup, hash outputs, Johnny result screens, and a separate NetworkWalks achievement image. They do not include dedicated captures of the NetworkWalks Hash Calculator or Password Cracker execution. Module 2 is therefore described from the supplied guide, not claimed as screenshot-verified. See the [evidence register](docs/EVIDENCE.md).

## Repository contents

```text
.
├── README.md
├── docs/
│   ├── Cybersecurity-Lab-Report.pdf
│   └── EVIDENCE.md
├── references/
│   └── SOURCES.md
└── screenshots/
    ├── 01-johnny-setup.jpg
    ├── 02-johnny-configuration.jpg
    ├── 03-john-ripper-run-folder.jpg
    ├── 04-pdf-hash-sample-1.jpg
    ├── 05-pdf-hash-sample-2.jpg
    ├── 06-johnny-audit-result-1.jpg
    ├── 07-johnny-audit-result-2.jpg
    └── 08-networkwalks-flag-achievement.jpg
```

## Documentation

- [Lab report (PDF)](docs/Cybersecurity-Lab-Report.pdf)
- [Evidence register](docs/EVIDENCE.md)
- [References and source notes](references/SOURCES.md)

## Screenshots

| Evidence | Screenshot |
|---|---|
| Johnny setup | ![Johnny setup](screenshots/01-johnny-setup.jpg) |
| Johnny configuration | ![Johnny configuration](screenshots/02-johnny-configuration.jpg) |
| John the Ripper run folder | ![JTR run folder](screenshots/03-john-ripper-run-folder.jpg) |
| PDF hash output — sample 1 | ![PDF hash sample 1](screenshots/04-pdf-hash-sample-1.jpg) |
| PDF hash output — sample 2 | ![PDF hash sample 2](screenshots/05-pdf-hash-sample-2.jpg) |
| Johnny audit result — 1 | ![Johnny result 1](screenshots/06-johnny-audit-result-1.jpg) |
| Johnny audit result — 2 | ![Johnny result 2](screenshots/07-johnny-audit-result-2.jpg) |
| NetworkWalks achievement (separate evidence) | ![NetworkWalks achievement](screenshots/08-networkwalks-flag-achievement.jpg) |

## Learning outcomes

- Understood the purpose of authorized PDF password auditing.
- Practiced the documented John the Ripper and Johnny desktop workflow.
- Reviewed PDF hash extraction output and the `$pdf$` hash format referenced in the guides.
- Studied a browser-based workflow using NetworkWalks tools.
- Learned to distinguish directly supplied evidence from steps documented only in a guide.

## Responsible use

This repository is for educational purposes and authorized security testing only. Test only documents you own or have explicit permission to assess. Do not publish recovered passwords, private documents, or sensitive hash data. Review the data-handling practices of any online service before uploading a document.

---

**Mohit Dinesh Sonawane** · Computer Engineering · SIEM
