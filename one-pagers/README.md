# One-pagers

Finished Dust Whisperers marketing sheets, US Letter (8.5 × 11 in).

## Customer two-pager

The front is the pitch. The back lists what each package cleans, room by room.

| File | Use |
|---|---|
| `customer/dust-whisperers-customer-two-pager-print.pdf` | Printing. Dark front, cream back. |
| `customer/dust-whisperers-customer-two-pager-posting.pdf` | Posting online, where both pages are seen together. Dark front, dark back. |
| `customer/dust-whisperers-customer-front.png` | The front as an image. |
| `customer/dust-whisperers-customer-back-cream.png` | The cream back as an image. |
| `customer/dust-whisperers-customer-back-dark.png` | The dark back as an image. |

## Cleaner one-pager

For individual cleaners who want to apply.

| File | Use |
|---|---|
| `cleaners/dust-whisperers-cleaner-one-pager.pdf` | Printing or attaching. |
| `cleaners/dust-whisperers-cleaner-one-pager.png` | Posting online. |
| `cleaners/dust-whisperers-cleaner-one-pager-es.pdf` | The Spanish version, for printing or attaching. |
| `cleaners/dust-whisperers-cleaner-one-pager-es.png` | The Spanish version, for posting online. |

## Cleaning companies one-pager

For cleaning companies that bring their own crew. Its link and QR code go to
the partner page at `contractor.dustwhisperers.com/partners`.

| File | Use |
|---|---|
| `cleaning-companies/dust-whisperers-cleaning-companies-one-pager.pdf` | Printing or attaching. |
| `cleaning-companies/dust-whisperers-cleaning-companies-one-pager.png` | Posting online. |
| `cleaning-companies/dust-whisperers-cleaning-companies-one-pager-es.pdf` | The Spanish version, for printing or attaching. |
| `cleaning-companies/dust-whisperers-cleaning-companies-one-pager-es.png` | The Spanish version, for posting online. |

## Spanish versions

The cleaner sheet and the cleaning companies sheet each have a Spanish version,
with `-es` in the file name. The wording follows the Spanish contractor site:
Texas Spanish, addressing the reader as `usted`. Their QR codes open the site
in Spanish (`?lang=es`).

The Spanish cleaner sheet lists one requirement the English sheet does not:
enough spoken English to deal directly with clients.

There is no Spanish version of the customer two-pager.

## Source

`source/` holds each sheet as a single HTML file, with its images in
`source/assets/`. The images are 1632 × 2112 pixels.

To rebuild a PDF, open the HTML file in Chrome and print to PDF with paper size
Letter, margins set to None and background graphics switched on.

The type is Cormorant Garamond and DM Sans, loaded from Google Fonts.

The room behind the top of the customer front, the cleaner sheet and the
cleaning companies sheet is `source/assets/living-room.jpg`, an illustrative
image.
