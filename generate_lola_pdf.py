#!/usr/bin/env python3
"""
Generate a delegated task PDF for Lola - BBS Sponsorship Link Research
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
import os

OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "LOLA-SPONSORSHIP-RESEARCH-TASK.pdf")

# Colors
DARK_BG = HexColor("#1a1a2e")
ACCENT = HexColor("#e94560")
ACCENT_LIGHT = HexColor("#f5e6cc")
HEADER_BG = HexColor("#16213e")
ROW_ALT = HexColor("#f7f7f7")
LINK_COLOR = HexColor("#0066cc")
GREEN = HexColor("#2d6a4f")
ORANGE = HexColor("#e76f51")
RED = HexColor("#c1121f")
LIGHT_GREEN = HexColor("#d8f3dc")
LIGHT_ORANGE = HexColor("#fde8d0")
LIGHT_RED = HexColor("#fcd5ce")

def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=letter,
        rightMargin=0.6*inch,
        leftMargin=0.6*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Title'],
        fontSize=22,
        leading=26,
        textColor=DARK_BG,
        spaceAfter=4,
        fontName='Helvetica-Bold'
    )

    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontSize=12,
        leading=16,
        textColor=HexColor("#555555"),
        spaceAfter=2,
        fontName='Helvetica'
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        leading=18,
        textColor=DARK_BG,
        spaceBefore=16,
        spaceAfter=8,
        fontName='Helvetica-Bold'
    )

    section_style = ParagraphStyle(
        'SectionHead',
        parent=styles['Heading3'],
        fontSize=11,
        leading=14,
        textColor=ACCENT,
        spaceBefore=12,
        spaceAfter=4,
        fontName='Helvetica-Bold'
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=9.5,
        leading=13,
        textColor=HexColor("#333333"),
        spaceAfter=6,
        fontName='Helvetica'
    )

    small_style = ParagraphStyle(
        'Small',
        parent=styles['Normal'],
        fontSize=8,
        leading=10,
        textColor=HexColor("#666666"),
        fontName='Helvetica'
    )

    link_style = ParagraphStyle(
        'Link',
        parent=styles['Normal'],
        fontSize=8.5,
        leading=11,
        textColor=LINK_COLOR,
        fontName='Helvetica'
    )

    bold_style = ParagraphStyle(
        'BoldBody',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    checklist_style = ParagraphStyle(
        'Checklist',
        parent=body_style,
        fontSize=9,
        leading=12,
        leftIndent=15,
        spaceAfter=3,
    )

    instruction_style = ParagraphStyle(
        'Instruction',
        parent=body_style,
        fontSize=9.5,
        leading=13,
        textColor=HexColor("#1a1a2e"),
        backColor=HexColor("#f0f4ff"),
        borderPadding=(6, 8, 6, 8),
        spaceAfter=8,
    )

    elements = []

    # ===== HEADER =====
    elements.append(Paragraph("BBS SPONSORSHIP RESEARCH", title_style))
    elements.append(Paragraph("Delegated Task Sheet for Lola", subtitle_style))
    elements.append(Paragraph("BIPOC Business Society | University of Ottawa | 2025-2026", small_style))
    elements.append(Spacer(1, 4))
    elements.append(HRFlowable(width="100%", thickness=2, color=ACCENT, spaceAfter=10))

    # ===== INSTRUCTIONS =====
    elements.append(Paragraph("YOUR TASK", heading_style))
    elements.append(Paragraph(
        "Go through each of the 25 links below. For every sponsor, confirm the following and fill in the checklist boxes. "
        "This research will directly feed into BBS's $50K+ sponsorship strategy for the 2025-2026 year.",
        body_style
    ))
    elements.append(Spacer(1, 4))

    elements.append(Paragraph("For EACH link, confirm:", section_style))
    checklist_items = [
        "Is the application/program still ACTIVE for 2025-2026?",
        "What is the exact DEADLINE or intake window?",
        "What is the MAXIMUM amount we can apply for?",
        "Does it require registered charity/nonprofit status? (If yes, note it - we need a fiscal sponsor)",
        "Is there an online portal? Copy the DIRECT application link.",
        "What documents/info do they need? (budget, constitution, letters of support, etc.)",
        "Any BIPOC/diversity-specific criteria or checkboxes we should know about?",
    ]
    for item in checklist_items:
        elements.append(Paragraph(f"\u2610  {item}", checklist_style))

    elements.append(Spacer(1, 6))
    elements.append(Paragraph(
        "<b>DEADLINE TO COMPLETE:</b> Return this document with your findings within <b>5 business days</b>. "
        "Flag anything marked URGENT immediately - some deadlines are in April 2025.",
        instruction_style
    ))

    elements.append(Spacer(1, 6))
    elements.append(HRFlowable(width="100%", thickness=1, color=HexColor("#cccccc"), spaceAfter=10))

    # ===== SPONSOR LINKS =====
    sponsors = [
        # TIER 1 - HIGH PRIORITY
        {
            "num": 1,
            "tier": "TIER 1 - HIGHEST PRIORITY",
            "name": "Scotiabank - ScotiaRISE / Community Sponsorship",
            "url": "https://www.scotiabank.com/ca/en/about/responsibility/community/sponsorships.html",
            "amount": "$5,000 - $10,000/year",
            "likelihood": "85%",
            "priority": "URGENT",
            "notes": "Apply under SPONSORSHIP track. Focus area: 'Remove Barriers to Career Advancement'. Multi-year (up to 5 years). Must register on Benevity Causes Portal. BIPOC KPI tracking built into their form."
        },
        {
            "num": 2,
            "name": "RBC - Community Sponsorship (Sponsorium)",
            "url": "https://www.rbc.com/community-social-impact/apply-for-funding/index.html",
            "amount": "$3,000 - $10,000",
            "likelihood": "80%",
            "priority": "URGENT",
            "notes": "Use Sponsorium platform. Select 'Organization' (NOT 'Event') as Sponsorship Opportunity Type. Year-round applications."
        },
        {
            "num": 3,
            "name": "RBC Future Launch - BIPOC Youth",
            "url": "https://www.rbc.com/en/future-launch/about/bipoc-youth/",
            "amount": "Partnership + $10K scholarships",
            "likelihood": "50%",
            "priority": "HIGH",
            "notes": "Explore becoming a nominating community partner for RBC Black Youth Scholarships ($10K/year per student). Check if student orgs can partner."
        },
        {
            "num": 4,
            "name": "BMO - Community Sponsorships / EMpower",
            "url": "https://www.bmo.com/en-ca/main/about-bmo/our-impact/communities/community-sponsorships/",
            "amount": "$2,000 - $5,000",
            "likelihood": "65%",
            "priority": "HIGH",
            "notes": "BMO EMpower = $100M+ commitment for BIPOC communities. Also email corporate.sponsorships@bmo.com. Check BMO Capital Markets Diversity sponsorships separately."
        },
        {
            "num": 5,
            "name": "TD Bank - Ready Commitment Funding",
            "url": "https://www.td.com/ca/en/about-td/ready-commitment/funding",
            "amount": "$2,000 - $5,000",
            "likelihood": "60%",
            "priority": "HIGH",
            "notes": "4 intake deadlines per year. TD does NOT fund general operating - must frame as a specific named program. Check if TD Ready Challenge has reopened for 2025-2026."
        },
        {
            "num": 6,
            "name": "CIBC - Community & Sponsorship Funding Guidelines",
            "url": "https://www.cibc.com/en/about-cibc/corporate-responsibility/community-and-sponsorship/funding-guidelines.html",
            "amount": "$1,000 - $5,000",
            "likelihood": "50%",
            "priority": "MEDIUM",
            "notes": "Application via Benevity platform. Check specific eligibility for student organizations. Contact CIBC Campus Relations (Ottawa) as well."
        },
        {
            "num": 7,
            "name": "Desjardins - Community Development Fund",
            "url": "https://www.desjardins.com/ca/about-us/community/index.jsp",
            "amount": "$500 - $5,000",
            "likelihood": "55%",
            "priority": "MEDIUM",
            "notes": "Contact LOCAL Ottawa Caisse Desjardins branch directly - they have discretionary budgets. Emphasize bilingual/francophone membership."
        },
        # TIER 2 - FOUNDATIONS & GRANTS
        {
            "num": 8,
            "tier": "TIER 2 - FOUNDATIONS & GRANTS",
            "name": "Ontario Trillium Foundation - Youth Opportunities Fund",
            "url": "https://otf.ca/our-grants/youth-opportunities-fund",
            "amount": "$5,000 - $150,000/year",
            "likelihood": "55%",
            "priority": "URGENT - DEADLINE APRIL 9",
            "notes": "Expression of Interest deadline: APRIL 9, 2025. Full app: July 9, 2025. Prioritizes Indigenous and Black youth. Scale grants up to $150K/year for 2-3 years. May need fiscal sponsor. Contact: yof@otf.ca"
        },
        {
            "num": 9,
            "name": "OTF - Youth Innovations Scale Grant (Detail Page)",
            "url": "https://otf.ca/our-grants/youth-opportunities-fund/youth-innovations-scale-grant",
            "amount": "Up to $150,000/year",
            "likelihood": "55%",
            "priority": "URGENT - DEADLINE APRIL 9",
            "notes": "This is the specific grant stream within OTF. Up to $150K/year for 2-3 years. Check if BBS qualifies as a youth-led group (ages 12-25)."
        },
        {
            "num": 10,
            "name": "Black Opportunity Fund (BOF)",
            "url": "https://blackopportunityfund.ca/",
            "amount": "$5,000 - $25,000",
            "likelihood": "60%",
            "priority": "HIGH",
            "notes": "Created specifically for Black-led/Black-serving orgs. Focus: economic empowerment, capacity building. Check current grant cycle and eligibility for student orgs."
        },
        {
            "num": 11,
            "name": "Community Foundation of Ottawa",
            "url": "https://www.ottawafoundation.org/",
            "amount": "$2,000 - $15,000",
            "likelihood": "65%",
            "priority": "HIGH",
            "notes": "LOCAL Ottawa foundation. Multiple grant streams (youth, diversity, community). Check all current open grant cycles and which ones BBS qualifies for."
        },
        {
            "num": 12,
            "name": "BlackNorth Initiative",
            "url": "https://blacknorth.ca/",
            "amount": "Connections to 500+ corporate sponsors",
            "likelihood": "55%",
            "priority": "MEDIUM",
            "notes": "500+ companies pledged 3% of donations to Black communities. Check if BBS can register as a community partner to access their corporate network and Vanguard Scholars program."
        },
        {
            "num": 13,
            "name": "Canadian Race Relations Foundation (CRRF)",
            "url": "https://www.crrf-fcrr.ca/",
            "amount": "$5,000 - $25,000",
            "likelihood": "40%",
            "priority": "MEDIUM",
            "notes": "Government-funded. Check for any open grant programs for projects addressing racial equity in business/education."
        },
        {
            "num": 14,
            "name": "GrantWatch - BIPOC Grants Ontario",
            "url": "https://ontario.grantwatch.com/cat/53/bipoc-grants.html",
            "amount": "Various",
            "likelihood": "N/A - Research Tool",
            "priority": "HIGH",
            "notes": "This is a grant AGGREGATOR. Scan the full list and note any grants BBS could apply to that are not already on this list. Look for Ontario-specific BIPOC funding."
        },
        # TIER 3 - CORPORATE RECRUITMENT PIPELINES
        {
            "num": 15,
            "tier": "TIER 3 - CORPORATE PARTNERSHIPS",
            "name": "Shopify - Social Impact / Community Partnerships",
            "url": "https://www.shopify.com/about/social-impact",
            "amount": "$3,000 - $10,000",
            "likelihood": "70%",
            "priority": "HIGH",
            "notes": "HQ in OTTAWA. Check if community/campus partnership applications are still active despite DEI rollbacks. Also check Shopify University Relations for recruitment sponsorships."
        },
        {
            "num": 16,
            "name": "Deloitte Canada - Community Impact / DEI",
            "url": "https://www.deloitte.com/ca/en/who-we-are/story/impact/diversity-equity-inclusion-and-accessibility.html",
            "amount": "$1,000 - $5,000",
            "likelihood": "75%",
            "priority": "HIGH",
            "notes": "Find Ottawa office campus recruiter contact. Check if they have a student org sponsorship application or if it's relationship-based. Note any DEI program changes."
        },
        {
            "num": 17,
            "name": "Osler - Black Future Lawyers / Diversity Programs",
            "url": "https://www.osler.com/en/about-us/media-centre/leading-law-firms-announce-1-75-million-long-term-commitment-to-black-future-lawyers/",
            "amount": "$500 - $2,000",
            "likelihood": "70%",
            "priority": "MEDIUM",
            "notes": "$1.75M commitment across 14 law firms for Black students. Check if business students (not just law) can access any funding. Get Ottawa office student programs contact."
        },
        {
            "num": 18,
            "name": "Accenture Canada - Community Impact",
            "url": "https://www.accenture.com/ca-en/about/company/canada-community-impact",
            "amount": "$1,000 - $5,000",
            "likelihood": "40%",
            "priority": "MEDIUM",
            "notes": "Check status of DEI programs after 2025 rollbacks. Look for Elevate to Innovate program and campus recruitment sponsorship options."
        },
        # TIER 4 - TELECOM & TECH
        {
            "num": 19,
            "tier": "TIER 4 - TELECOM & ADDITIONAL",
            "name": "Bell - Let's Talk Community Fund",
            "url": "https://letstalk.bell.ca/en/bell-lets-talk-community-fund",
            "amount": "$5,000 - $25,000",
            "likelihood": "45%",
            "priority": "MEDIUM",
            "notes": "MENTAL HEALTH focused. BBS would need to add wellness/mental health programming for BIPOC students. Check if student orgs can apply or if fiscal sponsor required."
        },
        {
            "num": 20,
            "name": "Rogers - Community Grants",
            "url": "https://about.rogers.com/giving-back/community-grants/",
            "amount": "$1,000 - $15,000",
            "likelihood": "50%",
            "priority": "MEDIUM",
            "notes": "Youth economic empowerment focus. Also check Ted Rogers Scholarship Fund. Confirm student org eligibility."
        },
        {
            "num": 21,
            "name": "TELUS - Community Boards (Ottawa)",
            "url": "https://www.telus.com/en/social-impact/giving-back/community-boards",
            "amount": "$5,000 - $20,000",
            "likelihood": "45%",
            "priority": "MEDIUM",
            "notes": "Local Ottawa volunteer board decides. Opens twice/year. Likely needs registered charity status - check. Focus: health, education, tech."
        },
        {
            "num": 22,
            "name": "Microsoft Canada - Philanthropies",
            "url": "https://www.microsoft.com/en-ca/about/philanthropies",
            "amount": "$1,000 - $3,000 + in-kind",
            "likelihood": "40%",
            "priority": "LOW",
            "notes": "Cash unlikely but in-kind valuable (free Microsoft 365, Azure credits). Check campus recruitment sponsorship separately."
        },
        {
            "num": 23,
            "name": "Google Canada - Conference Sponsorship for Underrepresented Groups",
            "url": "https://about.google/intl/en_ca/google-in-canada/",
            "amount": "$1,000 - $3,000",
            "likelihood": "40%",
            "priority": "LOW",
            "notes": "Google offers all-expenses-paid conference trips for underrepresented individuals. Check Google for Startups and campus recruitment team for Ottawa."
        },
        {
            "num": 24,
            "name": "Norton Rose Fulbright - Diversity & Inclusion Actions",
            "url": "https://www.nortonrosefulbright.com/en-ca/about/diversity-equity-and-inclusion/actions",
            "amount": "$500 - $2,000",
            "likelihood": "70%",
            "priority": "MEDIUM",
            "notes": "Has Ottawa office. Check student organization sponsorship process. Find Ottawa student recruitment coordinator contact info."
        },
        {
            "num": 25,
            "name": "Vancouver Foundation - LEVEL BIPOC Grants (Reference Model)",
            "url": "https://www.vancouverfoundation.ca/grant-seekers/find-grants/level-bipoc-grants/",
            "amount": "Up to $150,000 (BC only)",
            "likelihood": "0% (BC only)",
            "priority": "REFERENCE ONLY",
            "notes": "BBS cannot apply (BC only) but this is the GOLD STANDARD model for BIPOC grants in Canada. Study their application structure and criteria - use it as a template when approaching Ottawa/Ontario foundations."
        },
    ]

    current_tier = None

    for s in sponsors:
        # Tier header
        if "tier" in s and s["tier"] != current_tier:
            current_tier = s["tier"]
            elements.append(Spacer(1, 10))
            elements.append(Paragraph(current_tier, heading_style))
            elements.append(HRFlowable(width="100%", thickness=1.5, color=ACCENT, spaceAfter=8))

        # Priority color
        priority = s["priority"]
        if "URGENT" in priority:
            pri_color = RED
            pri_bg = LIGHT_RED
        elif priority == "HIGH":
            pri_color = ORANGE
            pri_bg = LIGHT_ORANGE
        else:
            pri_color = GREEN
            pri_bg = LIGHT_GREEN

        # Sponsor block
        num_text = f"<b>#{s['num']}</b>"
        name_text = f"<b>{s['name']}</b>"

        # Header row
        header_data = [[
            Paragraph(f"{num_text}  {name_text}", ParagraphStyle('SponsorName', parent=bold_style, fontSize=10, leading=13)),
            Paragraph(f"<b>{priority}</b>", ParagraphStyle('Priority', parent=small_style, fontSize=8, textColor=pri_color, alignment=TA_RIGHT)),
        ]]
        header_table = Table(header_data, colWidths=[5.2*inch, 1.8*inch])
        header_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ]))
        elements.append(header_table)

        # URL
        elements.append(Paragraph(f'<link href="{s["url"]}">{s["url"]}</link>', link_style))

        # Details row
        detail_data = [[
            Paragraph(f"<b>Ask:</b> {s['amount']}", small_style),
            Paragraph(f"<b>Likelihood:</b> {s['likelihood']}", small_style),
        ]]
        detail_table = Table(detail_data, colWidths=[3.5*inch, 3.5*inch])
        detail_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 1),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ]))
        elements.append(detail_table)

        # Notes
        elements.append(Paragraph(f"<b>Notes:</b> {s['notes']}", small_style))

        # Checklist
        elements.append(Spacer(1, 3))
        check_data = [
            [Paragraph("\u2610 Active?", small_style),
             Paragraph("\u2610 Deadline confirmed?", small_style),
             Paragraph("\u2610 Max amount?", small_style),
             Paragraph("\u2610 Docs needed?", small_style)],
        ]
        check_table = Table(check_data, colWidths=[1.75*inch, 1.75*inch, 1.75*inch, 1.75*inch])
        check_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 1),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
            ('BACKGROUND', (0, 0), (-1, -1), HexColor("#f8f8f8")),
            ('BOX', (0, 0), (-1, -1), 0.5, HexColor("#dddddd")),
        ]))
        elements.append(check_table)

        # Lola's notes field
        elements.append(Spacer(1, 2))
        notes_data = [[Paragraph("<b>Lola's Findings:</b> _______________________________________________________________________________", small_style)]]
        notes_table = Table(notes_data, colWidths=[7*inch])
        notes_table.setStyle(TableStyle([
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('BACKGROUND', (0, 0), (-1, -1), HexColor("#fffef5")),
            ('BOX', (0, 0), (-1, -1), 0.5, HexColor("#dddddd")),
        ]))
        elements.append(notes_table)

        elements.append(Spacer(1, 10))
        elements.append(HRFlowable(width="100%", thickness=0.5, color=HexColor("#eeeeee"), spaceAfter=6))

    # ===== SUMMARY PAGE =====
    elements.append(PageBreak())
    elements.append(Paragraph("SUMMARY CHECKLIST", heading_style))
    elements.append(HRFlowable(width="100%", thickness=2, color=ACCENT, spaceAfter=10))
    elements.append(Paragraph(
        "Once you have gone through all 25 links, fill out this summary and return to Nathan.",
        body_style
    ))
    elements.append(Spacer(1, 8))

    summary_headers = ["#", "Sponsor", "Still Active?", "Deadline", "Max $", "Can We Apply?"]
    summary_data = [summary_headers]
    for s in sponsors:
        summary_data.append([
            str(s["num"]),
            s["name"][:35] + ("..." if len(s["name"]) > 35 else ""),
            "\u2610 Y  \u2610 N",
            "",
            "",
            "\u2610 Y  \u2610 N"
        ])

    summary_table = Table(summary_data, colWidths=[0.35*inch, 2.4*inch, 0.9*inch, 1.1*inch, 0.85*inch, 0.9*inch])
    summary_table.setStyle(TableStyle([
        # Header
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_BG),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 7),
        # Body
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 6.5),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#cccccc")),
        # Alternating rows
        *[('BACKGROUND', (0, i), (-1, i), ROW_ALT) for i in range(2, len(summary_data), 2)],
    ]))
    elements.append(summary_table)

    elements.append(Spacer(1, 20))
    elements.append(Paragraph("<b>Total Sponsors Confirmed Active:</b> ______ / 25", body_style))
    elements.append(Paragraph("<b>Total Potential Revenue Identified:</b> $ ______________", body_style))
    elements.append(Paragraph("<b>Urgent Deadlines Found:</b> _______________________________________________", body_style))
    elements.append(Spacer(1, 12))
    elements.append(HRFlowable(width="100%", thickness=1, color=HexColor("#cccccc"), spaceAfter=8))
    elements.append(Paragraph("<b>Completed by:</b> Lola", body_style))
    elements.append(Paragraph("<b>Date Completed:</b> ____________________", body_style))
    elements.append(Paragraph("<b>Return to:</b> Nathan Amankwah (Finance Pillar, BBS)", body_style))

    # Build
    doc.build(elements)
    print(f"PDF generated: {OUTPUT_PATH}")

if __name__ == "__main__":
    build_pdf()
