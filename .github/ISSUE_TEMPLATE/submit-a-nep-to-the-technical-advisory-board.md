---
name: Submit a NEP to the Technical Advisory Board
about: ''
title: ''
labels: New Proposal
assignees: ''

---
body:
  - type: markdown
    attributes:
      value: |
        Thank you for submitting an NWB Extension Proposal to the Technical Advisory Board!
  - type: input
    id: name
    attributes:
      label: NEP Title
      description: What is the NEP number and title? Please also use this as the title for this issue ticket.
      placeholder: ex. NEP000: My Awesome Neurodata Type
    validations:
      required: false
  - type: input
    id: nep_link
    attributes:
      label: Link to NEP
      description: Provide a link to the publicly accessible Google Doc or other doc with the NEP.
      placeholder: ex. https://docs.google.com/...
    validations:
      required: true
  - type: textarea
    id: summary
    attributes:
      label: NEP Summary
      description: Copy and paste the NEP summary here.
      placeholder: ex. My Awesome Neurodata Type is necessary for awesome science.
    validations:
      required: true
  - type: input
    id: contact_name
    attributes:
      label: Point of Contact Name
      description: Who should we get in touch with if we need more info?
      placeholder: ex. Jane Doe
    validations:
      required: true
  - type: input
    id: contact_email
    attributes:
      label: Point of Contact Email
      description: How can we get in touch with the point of contact if we need more info?
      placeholder: ex. email@example.com
    validations:
      required: true
