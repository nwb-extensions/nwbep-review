# NWBEP Review Form Template

This directory contains a [Copier](https://copier.readthedocs.io/) template for generating pre-filled NWBEP review forms.

## Usage

To generate a review form for a specific reviewer, run from the repository root:

```bash
uvx copier copy templates/ NWBEPXXX/reviews/ --data nwbep_number=XXX
```

Copier will prompt for the remaining fields (title, reviewer name, affiliation, ORCID).
To skip prompts, pass all values on the command line:

```bash
uvx copier copy templates/ NWBEP004/reviews/ \
    --data nwbep_number=004 \
    --data "nwbep_title=Optical Devices and Microscopy" \
    --data "reviewer_name=Jane Doe" \
    --data "reviewer_affiliation=University of Example" \
    --data "reviewer_orcid=0000-0000-0000-1234"
```

Then rename the generated file to include the reviewer's initials:

```bash
mv NWBEP004/reviews/NWBEP-review-form.md NWBEP004/reviews/NWBEP004-review-JD.md
```
