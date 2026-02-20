#!/usr/bin/env python3
"""
Generate Banking Options PDF for BBS Club President Shaan Haque
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
import os

OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "BBS-BANKING-OPTIONS-SHAAN.pdf")

DARK_BG = HexColor("#1a1a2e")
ACCENT = HexColor("#e94560")
HEADER_BG = HexColor("#16213e")
ROW_ALT = HexColor("#f7f7f7")
LINK_COLOR = HexColor("#0066cc")
GREEN = HexColor("#2d6a4f")
ORANGE = HexColor("#e76f51")
RED = HexColor("#c1121f")
GOLD = HexColor("#b8860b")
LIGHT_GREEN = HexColor("#d8f3dc")
LIGHT_BLUE = HexColor("#e8f0fe")

def build_pdf():
    doc = SimpleDocTemplate(OUTPUT_PATH, pagesize=letter, rightMargin=0.6*inch, leftMargin=0.6*inch, topMargin=0.5*inch, bottomMargin=0.5*inch)
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle('T', parent=styles['Title'], fontSize=22, leading=26, textColor=DARK_BG, spaceAfter=4, fontName='Helvetica-Bold')
    subtitle_style = ParagraphStyle('ST', parent=styles['Normal'], fontSize=12, leading=16, textColor=HexColor("#555555"), spaceAfter=2, fontName='Helvetica')
    heading_style = ParagraphStyle('H', parent=styles['Heading2'], fontSize=14, leading=18, textColor=DARK_BG, spaceBefore=14, spaceAfter=8, fontName='Helvetica-Bold')
    section_style = ParagraphStyle('S', parent=styles['Heading3'], fontSize=11, leading=14, textColor=ACCENT, spaceBefore=10, spaceAfter=4, fontName='Helvetica-Bold')
    body_style = ParagraphStyle('B', parent=styles['Normal'], fontSize=9.5, leading=13, textColor=HexColor("#333333"), spaceAfter=6, fontName='Helvetica')
    small_style = ParagraphStyle('SM', parent=styles['Normal'], fontSize=8, leading=10, textColor=HexColor("#666666"), fontName='Helvetica')
    bold_style = ParagraphStyle('BD', parent=body_style, fontName='Helvetica-Bold')
    link_style = ParagraphStyle('L', parent=styles['Normal'], fontSize=8.5, leading=11, textColor=LINK_COLOR, fontName='Helvetica')
    rec_style = ParagraphStyle('REC', parent=body_style, fontSize=10, leading=14, textColor=GREEN, fontName='Helvetica-Bold', backColor=LIGHT_GREEN, borderPadding=(8, 10, 8, 10))
    callout_style = ParagraphStyle('CO', parent=body_style, fontSize=9.5, leading=13, textColor=DARK_BG, backColor=LIGHT_BLUE, borderPadding=(8, 10, 8, 10), spaceAfter=10)
    num_style = ParagraphStyle('NUM', parent=bold_style, fontSize=18, leading=22, textColor=ACCENT, fontName='Helvetica-Bold')

    elements = []

    # ===== HEADER =====
    elements.append(Paragraph("BBS BANKING OPTIONS", title_style))
    elements.append(Paragraph("For Shaan Haque, President | BIPOC Business Society", subtitle_style))
    elements.append(Paragraph("Prepared by Nathan Amankwah, Finance Pillar | February 2026", small_style))
    elements.append(Spacer(1, 4))
    elements.append(HRFlowable(width="100%", thickness=2, color=ACCENT, spaceAfter=12))

    # ===== CONTEXT =====
    elements.append(Paragraph("SITUATION", heading_style))
    elements.append(Paragraph(
        "The current BBS bank account (ending in 1726) is locked. We need a new bank account that is simple, "
        "low/no fee, and easy for a student-run club to manage. Below are the best options in Ottawa ranked by fit for BBS.",
        body_style
    ))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph(
        "When you walk into any of these banks, say: \"We're a student-run club under AETSA at the University of Ottawa "
        "Telfer School of Management. We need a community or not-for-profit chequing account.\" They will know exactly what to set up.",
        callout_style
    ))

    # ===== WHAT TO BRING =====
    elements.append(Paragraph("WHAT TO BRING TO THE BANK", section_style))
    bring_items = [
        "Club constitution (in your files: BBS Finances 2024-2025/1. Club Constitution/)",
        "Two pieces of government-issued ID (yours as President + one other signing officer)",
        "Proof of club registration with AETSA/UOSU (letter or screenshot)",
        "Meeting minutes showing you were elected President",
        "BBS mailing address (use Telfer School of Management address)",
    ]
    for item in bring_items:
        elements.append(Paragraph(f"\u2022  {item}", body_style))

    elements.append(Spacer(1, 6))
    elements.append(HRFlowable(width="100%", thickness=1, color=HexColor("#cccccc"), spaceAfter=10))

    # ===== TOP RECOMMENDATION =====
    elements.append(Paragraph("TOP RECOMMENDATION", heading_style))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=GREEN, spaceAfter=8))

    elements.append(Paragraph("TD Community / Not-For-Profit Banking Plan", ParagraphStyle('RN', parent=bold_style, fontSize=14, leading=18, textColor=GREEN)))
    elements.append(Spacer(1, 4))

    rec_data = [
        ["Monthly Fee", "$0 with $5,000 minimum balance OR ~$5/month without"],
        ["Transactions", "25 included per month (more than enough for BBS)"],
        ["E-Transfers", "Included"],
        ["Why #1 Pick", "BBS already has TD sponsorship docs on file. TD branch at 99 Bank St is 10 min walk from Telfer. Easiest transition."],
        ["Location", "TD Canada Trust - 99 Bank Street, Ottawa (closest to Telfer)"],
        ["Website", "td.com/ca/en/business-banking/small-business/bank-accounts/community-not-for-profit-plan"],
        ["Phone", "Book appointment at any TD branch or call 1-866-222-3456"],
    ]
    for row in rec_data:
        elements.append(Paragraph(f"<b>{row[0]}:</b> {row[1]}", body_style))
    elements.append(Spacer(1, 6))
    elements.append(Paragraph(
        "VERDICT: Best overall pick. Low friction, closest branch, existing relationship with TD through sponsorship work.",
        rec_style
    ))

    elements.append(Spacer(1, 12))
    elements.append(HRFlowable(width="100%", thickness=1, color=HexColor("#cccccc"), spaceAfter=10))

    # ===== ALL OPTIONS =====
    elements.append(Paragraph("ALL OPTIONS RANKED", heading_style))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=ACCENT, spaceAfter=8))

    banks = [
        {
            "rank": "1",
            "name": "TD Community / Not-For-Profit Plan",
            "fee": "$0 with $5K balance | ~$5/mo without",
            "transactions": "25/month included",
            "etransfers": "Included",
            "pros": "Closest branch to Telfer (99 Bank St). BBS already has TD docs. Well-known NFP plan. Easy to set up.",
            "cons": "Fee kicks in if balance drops below $5K.",
            "url": "https://www.td.com/ca/en/business-banking/small-business/bank-accounts/community-not-for-profit-plan",
            "verdict": "BEST OVERALL",
            "verdict_color": GREEN,
        },
        {
            "rank": "2",
            "name": "BMO Community Account",
            "fee": "$3.50/month (low-cost) | may waive for student clubs",
            "transactions": "15/month included, $0.65 each after",
            "etransfers": "$1.50 each (or free with add-on)",
            "pros": "Designed for not-for-profits. BMO branch at 131 Bank St near Telfer. BMO EMpower program = potential sponsor too.",
            "cons": "Small monthly fee. E-transfers cost extra unless bundled.",
            "url": "https://www.bmo.com/main/business/accounts/community-account/",
            "verdict": "STRONG RUNNER-UP",
            "verdict_color": ORANGE,
        },
        {
            "rank": "3",
            "name": "CIBC Not-For-Profit Operating Account",
            "fee": "$0 with $5K balance | ~$6/mo without",
            "transactions": "20/month included",
            "etransfers": "Included",
            "pros": "No fee if you hold $5K. CIBC has branches on Bank St. Clean digital banking app.",
            "cons": "$5K minimum is same as TD but CIBC has less of an existing relationship with BBS.",
            "url": "https://www.cibc.com/en/business/accounts/not-for-profit-operating-account.html",
            "verdict": "SOLID OPTION",
            "verdict_color": ORANGE,
        },
        {
            "rank": "4",
            "name": "RBC Royal Business Community Account",
            "fee": "$6.95/month | first 3 months FREE",
            "transactions": "15/month included",
            "etransfers": "Included",
            "pros": "RBC is a top sponsorship target for BBS. Having an RBC account deepens the relationship. Branch at 90 Sparks St.",
            "cons": "Highest monthly fee of the options. Only 15 transactions.",
            "url": "https://www.rbcroyalbank.com/business/accounts/community-account.html",
            "verdict": "GOOD IF PURSUING RBC SPONSORSHIP",
            "verdict_color": GOLD,
        },
        {
            "rank": "5",
            "name": "Alterna Savings Credit Union",
            "fee": "Likely $0-$4/month for community groups",
            "transactions": "Varies by plan",
            "etransfers": "Included in most plans",
            "pros": "Ottawa-based credit union. Community-focused values align with BBS mission. Multiple Ottawa branches.",
            "cons": "Less well-known. Need to visit branch to confirm exact club account terms.",
            "url": "https://www.alterna.ca/",
            "verdict": "WORTH EXPLORING - LOCAL OPTION",
            "verdict_color": GOLD,
        },
        {
            "rank": "6",
            "name": "Desjardins (Ottawa Caisse)",
            "fee": "~$7/month for business, may reduce for NFP",
            "transactions": "Varies by plan",
            "etransfers": "Included",
            "pros": "Bilingual. Strong community focus. Desjardins is also a potential sponsor. Ottawa branch on Laurier Ave.",
            "cons": "Higher base fee. Need to negotiate NFP rate in person. French-first institution.",
            "url": "https://www.desjardins.com/ca/your-credit-union/ontario/branches/ottawa/index.jsp",
            "verdict": "NICHE - GOOD IF BILINGUAL ANGLE MATTERS",
            "verdict_color": GOLD,
        },
    ]

    for b in banks:
        # Rank + Name header
        rank_name = [[
            Paragraph(f"<b>#{b['rank']}</b>", num_style),
            Paragraph(f"<b>{b['name']}</b>", ParagraphStyle('BN2', parent=bold_style, fontSize=12, leading=16, textColor=DARK_BG)),
        ]]
        rn_table = Table(rank_name, colWidths=[0.4*inch, 6.6*inch])
        rn_table.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 2)]))
        elements.append(rn_table)

        # Link
        elements.append(Paragraph(f'<link href="{b["url"]}">{b["url"]}</link>', link_style))
        elements.append(Spacer(1, 3))

        # Details grid
        details = [
            ["Monthly Fee", b["fee"]],
            ["Transactions", b["transactions"]],
            ["E-Transfers", b["etransfers"]],
        ]
        for d in details:
            elements.append(Paragraph(f"<b>{d[0]}:</b>  {d[1]}", small_style))

        elements.append(Spacer(1, 3))
        elements.append(Paragraph(f"<b>Pros:</b> {b['pros']}", ParagraphStyle('PR', parent=small_style, textColor=GREEN)))
        elements.append(Paragraph(f"<b>Cons:</b> {b['cons']}", ParagraphStyle('CN', parent=small_style, textColor=RED)))
        elements.append(Spacer(1, 4))

        # Verdict
        verdict_style = ParagraphStyle('V', parent=small_style, fontSize=9, textColor=b["verdict_color"], fontName='Helvetica-Bold')
        elements.append(Paragraph(f"VERDICT: {b['verdict']}", verdict_style))

        elements.append(Spacer(1, 8))
        elements.append(HRFlowable(width="100%", thickness=0.5, color=HexColor("#eeeeee"), spaceAfter=8))

    # ===== COMPARISON TABLE =====
    elements.append(PageBreak())
    elements.append(Paragraph("SIDE-BY-SIDE COMPARISON", heading_style))
    elements.append(HRFlowable(width="100%", thickness=2, color=ACCENT, spaceAfter=10))

    comp_headers = ["Bank", "Monthly Fee", "Transactions", "E-Transfers", "Verdict"]
    comp_data = [comp_headers]
    comp_rows = [
        ["TD NFP Plan", "$0 w/ $5K bal", "25/mo", "Free", "BEST"],
        ["BMO Community", "$3.50/mo", "15/mo", "$1.50 ea", "RUNNER-UP"],
        ["CIBC NFP", "$0 w/ $5K bal", "20/mo", "Free", "SOLID"],
        ["RBC Community", "$6.95/mo", "15/mo", "Free", "IF RBC SPONSOR"],
        ["Alterna CU", "~$0-$4/mo", "Varies", "Free", "LOCAL PICK"],
        ["Desjardins", "~$7/mo", "Varies", "Free", "BILINGUAL"],
    ]
    for r in comp_rows:
        comp_data.append(r)

    comp_table = Table(comp_data, colWidths=[1.2*inch, 1.2*inch, 1.0*inch, 1.0*inch, 1.6*inch])
    comp_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_BG),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor("#cccccc")),
        ('BACKGROUND', (0, 1), (-1, 1), LIGHT_GREEN),
        ('FONTNAME', (0, 1), (-1, 1), 'Helvetica-Bold'),
        *[('BACKGROUND', (0, i), (-1, i), ROW_ALT) for i in range(3, len(comp_data), 2)],
    ]))
    elements.append(comp_table)

    # ===== ACTION STEPS =====
    elements.append(Spacer(1, 20))
    elements.append(Paragraph("NEXT STEPS FOR SHAAN", heading_style))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=ACCENT, spaceAfter=8))

    steps = [
        ("Step 1", "Pick a bank from this list (TD recommended)"),
        ("Step 2", "Gather documents: club constitution, AETSA registration proof, two IDs, meeting minutes"),
        ("Step 3", "Book an appointment at the branch (or walk in)"),
        ("Step 4", "Tell them: \"Student-run club under AETSA at uOttawa Telfer. Need a community/not-for-profit chequing account.\""),
        ("Step 5", "Set up TWO signing officers on the account (President + Finance VP)"),
        ("Step 6", "Get a debit card and set up online banking"),
        ("Step 7", "Send Nathan the new account details for financial records"),
    ]
    for step_label, step_text in steps:
        step_data = [[
            Paragraph(f"<b>{step_label}</b>", ParagraphStyle('SL', parent=small_style, textColor=ACCENT, fontName='Helvetica-Bold')),
            Paragraph(step_text, body_style),
        ]]
        step_table = Table(step_data, colWidths=[0.8*inch, 6.2*inch])
        step_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ]))
        elements.append(step_table)

    elements.append(Spacer(1, 16))
    elements.append(HRFlowable(width="100%", thickness=1, color=HexColor("#cccccc"), spaceAfter=8))
    elements.append(Paragraph("<b>Prepared by:</b> Nathan Amankwah, Finance Pillar", body_style))
    elements.append(Paragraph("<b>For:</b> Shaan Haque, President, BIPOC Business Society", body_style))
    elements.append(Paragraph("<b>Date:</b> February 2026", body_style))
    elements.append(Paragraph("<b>Action Required:</b> Open new account ASAP so sponsorship deposits have somewhere to go", ParagraphStyle('AR', parent=body_style, textColor=RED, fontName='Helvetica-Bold')))

    doc.build(elements)
    print(f"PDF generated: {OUTPUT_PATH}")

if __name__ == "__main__":
    build_pdf()
