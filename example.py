"""
example_comprehensive.py
------------------------
Professional enterprise-grade report demonstrating docpilot's full capabilities.
Generates a comprehensive Quarterly Business Review (QBR) document.

Run: python example_comprehensive.py
Output: quarterly_business_review_q3_2025.pdf
"""

from docpilot import Report, BrandStyles
import pandas as pd
from datetime import datetime

# =============================================================================
# CONFIGURATION
# =============================================================================

# Define custom brand colors for a professional financial services look
BRAND = BrandStyles(
    primary="#1a365d",      # Deep navy blue
    secondary="#c53030",    # Corporate red
    accent="#d69e2e",       # Gold accent
)

COMPANY_NAME = "Apex Technologies Inc."
REPORT_TITLE = "Quarterly Business Review"
REPORT_PERIOD = "Q3 2025"
CONFIDENTIALITY = "Strictly Confidential - Internal Use Only"

# =============================================================================
# SAMPLE DATA
# =============================================================================

# Financial Performance Data
financial_summary = pd.DataFrame({
    "Metric": ["Total Revenue", "Gross Profit", "Operating Income", "Net Income", "EBITDA"],
    "Q3 2025 ($M)": ["$127.5", "$89.2", "$34.8", "$28.4", "$42.1"],
    "Q2 2025 ($M)": ["$118.3", "$82.1", "$30.2", "$24.6", "$38.5"],
    "Q3 2024 ($M)": ["$105.2", "$71.8", "$24.5", "$19.8", "$31.2"],
    "YoY Growth": ["+21.2%", "+24.2%", "+42.0%", "+43.4%", "+35.0%"],
})

# Revenue by Product Line
product_revenue = pd.DataFrame({
    "Product Line": ["Enterprise SaaS", "Cloud Infrastructure", "Consulting Services", "Support & Maintenance"],
    "Q3 Revenue ($M)": ["$58.2", "$42.7", "$18.9", "$7.7"],
    "% of Total": ["45.6%", "33.5%", "14.8%", "6.0%"],
    "Growth (QoQ)": ["+12.4%", "+8.7%", "+15.2%", "+3.1%"],
})

# Key Performance Indicators
kpis = pd.DataFrame({
    "KPI": ["Customer Acquisition Cost", "Lifetime Value", "Monthly Churn Rate", "Net Promoter Score", "Employee Satisfaction"],
    "Q3 2025": ["$1,240", "$48,500", "2.1%", "+67", "4.3/5.0"],
    "Target": ["$1,500", "$45,000", "<3.0%", ">+60", ">4.0/5.0"],
    "Status": ["✓ Exceeds", "✓ Exceeds", "✓ On Target", "✓ Exceeds", "✓ On Target"],
})

# Project Portfolio
projects = pd.DataFrame({
    "Project": ["Platform 2.0 Migration", "AI Analytics Suite", "Security Overhaul", "Mobile App Redesign"],
    "Status": ["In Progress", "Complete", "In Progress", "Planned"],
    "Budget ($M)": ["$8.5", "$4.2", "$6.0", "$3.5"],
    "Spent ($M)": ["$5.2", "$4.1", "$2.8", "$0.0"],
    "Completion": ["65%", "100%", "45%", "0%"],
    "Risk Level": ["Medium", "Low", "High", "Medium"],
})

# Risk Register
risk_register = [
    ["Risk Factor", "Likelihood", "Impact", "Mitigation Status"],
    ["Vendor dependency for cloud services", "Medium", "High", "Multi-cloud strategy implemented"],
    ["Key personnel turnover", "Medium", "Medium", "Succession planning in progress"],
    ["Cybersecurity threats", "High", "High", "Security overhaul underway (45% complete)"],
    ["Economic downturn impact on IT spending", "Medium", "Medium", "Diversifying client base"],
    ["Regulatory compliance (GDPR/SOC2)", "Low", "High", "Audit scheduled for Q4"],
]

# Team Structure
teams = pd.DataFrame({
    "Department": ["Engineering", "Product", "Sales", "Marketing", "Customer Success", "Operations"],
    "Headcount": ["142", "28", "45", "22", "38", "15"],
    "New Hires (Q3)": ["12", "3", "5", "2", "4", "1"],
    "Open Positions": ["8", "2", "6", "1", "3", "0"],
    "Avg Tenure (Years)": ["3.2", "2.8", "2.1", "1.9", "2.5", "4.1"],
})

# Quarterly Milestones
milestones = [
    ["Milestone", "Target Date", "Actual Date", "Status", "Owner"],
    ["Launch AI Analytics Suite", "Aug 15, 2025", "Aug 12, 2025", "✓ Complete", "J. Martinez"],
    ["Close Series C Funding", "Sep 30, 2025", "Sep 28, 2025", "✓ Complete", "A. Thompson"],
    ["Achieve SOC 2 Type II", "Sep 30, 2025", "—", "⏳ In Progress", "R. Kumar"],
    ["Open APAC Office", "Oct 15, 2025", "—", "📅 Planned", "S. Chen"],
    ["Release Mobile App v3.0", "Nov 30, 2025", "—", "📅 Planned", "M. Rodriguez"],
]

# Customer Metrics
customer_metrics = pd.DataFrame({
    "Segment": ["Enterprise ($500K+)", "Mid-Market ($50K-$500K)", "SMB (<$50K)"],
    "Active Customers": ["24", "156", "1,240"],
    "Q3 New Customers": ["3", "18", "89"],
    "Churn Rate": ["0%", "1.2%", "3.8%"],
    "Avg Contract Value": ["$892K", "$127K", "$12K"],
    "NPS Score": ["+78", "+65", "+52"],
})

# =============================================================================
# BUILD THE REPORT
# =============================================================================

# Initialize the report with professional branding
rpt = Report(
    "quarterly_business_review_q3_2025.pdf",
    title=f"{REPORT_TITLE} - {REPORT_PERIOD}",
    company=COMPANY_NAME,
    confidentiality=CONFIDENTIALITY,
    brand=BRAND,
)

# -----------------------------------------------------------------------------
# PAGE 1: COVER PAGE
# -----------------------------------------------------------------------------
rpt.title_block(
    REPORT_TITLE,
    subtitle=f"{COMPANY_NAME} | {REPORT_PERIOD}",
    date="October 15, 2025",
    version="Final",
)

rpt.section(
    "",
    "This document contains confidential and proprietary information of "
    f"{COMPANY_NAME}. Distribution is restricted to authorized personnel only.",
)

rpt.spacer(20)

# Document metadata table
meta_data = [
    ["Prepared By", "Office of the Chief Executive"],
    ["Reviewed By", "Board of Directors"],
    ["Distribution", "Executive Team, Board Members, Investors"],
    ["Classification", CONFIDENTIALITY],
]
rpt.table("Document Information", meta_data, caption="Distribution and classification details.")

rpt.page_break()

# -----------------------------------------------------------------------------
# PAGE 2: EXECUTIVE SUMMARY
# -----------------------------------------------------------------------------
rpt.title_block("Executive Summary", subtitle="Key Highlights & Strategic Overview")

exec_summary_body = (
    "<b>{company}</b> delivered exceptional results in {period}, demonstrating robust "
    "growth across all key business segments. Revenue reached an all-time high of "
    "<b>$127.5 million</b>, representing a 21.2% increase year-over-year and 7.8% growth "
    "quarter-over-quarter."
    "<br/><br/>"
    "Our strategic investments in artificial intelligence and cloud infrastructure have "
    "yielded significant returns, with the AI Analytics Suite achieving 100% completion "
    "ahead of schedule. Customer satisfaction metrics continue to exceed industry "
    "benchmarks, with an overall Net Promoter Score of +67."
    "<br/><br/>"
    "The company successfully closed <b>Series C funding of $75 million</b> led by "
    "top-tier venture capital firms, providing capital runway for accelerated expansion "
    "into the APAC market."
).format(company=COMPANY_NAME, period=REPORT_PERIOD)

rpt.section("", exec_summary_body)

rpt.bullets("Key Achievements", [
    f"Revenue growth of 21.2% YoY to $127.5M — highest quarterly revenue in company history",
    "Gross margin expansion to 70.0%, up 230 basis points from prior year",
    "Successful completion of Series C funding round ($75M at $850M valuation)",
    "Launch of AI Analytics Suite generating $4.2M in first-month bookings",
    "Zero churn among enterprise customers (>$500K ACV)",
    "Employee satisfaction score of 4.3/5.0 with reduced voluntary turnover",
])

rpt.bullets("Areas of Focus", [
    "Security infrastructure upgrade 45% complete — on track for Q4 completion",
    "APAC expansion delayed by 2 weeks due to regulatory approvals",
    "Mid-market customer churn at 1.2% — below target but requires monitoring",
    "Engineering headcount 8 positions behind plan — hiring accelerator initiated",
])

rpt.page_break()

# -----------------------------------------------------------------------------
# PAGE 3: FINANCIAL PERFORMANCE
# -----------------------------------------------------------------------------
rpt.title_block("Financial Performance", subtitle="Q3 2025 Financial Results")

rpt.section(
    "Overview",
    "The company delivered strong financial performance across all metrics, with revenue "
    "growth accelerating and profitability expanding significantly. Operating leverage "
    "improved as we scaled infrastructure investments made in prior quarters.",
)

rpt.table("Financial Summary", financial_summary, caption="Quarterly financial performance comparison (in millions USD).")

rpt.spacer()

rpt.section(
    "Revenue Analysis",
    "Revenue diversification continues with Enterprise SaaS maintaining its position as "
    "the primary growth driver. Cloud Infrastructure showed solid 8.7% QoQ growth, "
    "while Consulting Services outperformed expectations with 15.2% growth driven by "
    "AI implementation projects.",
)

rpt.table("Revenue by Product Line", product_revenue, caption="Product line breakdown and growth metrics.")

rpt.page_break()

# -----------------------------------------------------------------------------
# PAGE 4: KEY PERFORMANCE INDICATORS
# -----------------------------------------------------------------------------
rpt.title_block("Key Performance Indicators", subtitle="Operational Metrics & Targets")

rpt.section(
    "Performance Dashboard",
    "All critical KPIs met or exceeded targets for the quarter. Unit economics continue "
    "to improve with Customer Acquisition Cost declining 12% YoY while Lifetime Value "
    "increased 18%. The combination of reduced CAC and increased LTV has improved our "
    "LTV:CAC ratio to 39:1, well above the industry benchmark of 3:1.",
)

rpt.table("KPI Dashboard", kpis, caption="Q3 2025 KPI performance vs. targets.")

rpt.spacer()

rpt.bullets("Operational Highlights", [
    "Monthly recurring revenue (MRR) reached $42.1M, up 8.3% QoQ",
    "Gross revenue retention improved to 97.8% (from 96.2% in Q2)",
    "Net revenue retention reached 124% driven by upsell/cross-sell initiatives",
    "Sales cycle shortened to 67 days (from 78 days in Q2)",
    "Customer support ticket resolution time: 4.2 hours average",
    "Platform uptime: 99.97% (exceeding 99.9% SLA commitment)",
])

rpt.page_break()

# -----------------------------------------------------------------------------
# PAGE 5: CUSTOMER ANALYSIS
# -----------------------------------------------------------------------------
rpt.title_block("Customer Analysis", subtitle="Segment Performance & Satisfaction")

rpt.section(
    "Segment Overview",
    "Customer base expansion accelerated across all segments. Enterprise segment "
    "demonstrated exceptional loyalty with zero churn and three new logo wins including "
    "two Fortune 500 companies. Mid-market segment grew 13% with strong expansion revenue "
    "from existing accounts.",
)

rpt.table("Customer Metrics by Segment", customer_metrics, caption="Performance breakdown by customer segment.")

rpt.spacer()

rpt.section(
    "Customer Success Stories",
    "Notable wins this quarter include a $2.4M three-year contract with a leading "
    "healthcare provider and expansion of our relationship with a top-5 financial "
    "institution, adding $890K in annual recurring revenue. The AI Analytics Suite "
    "has been particularly well-received, with 87% of trial users converting to paid "
    "subscriptions.",
)

rpt.bullets("Customer Feedback Themes", [
    "Ease of implementation and integration with existing systems",
    "Quality and responsiveness of technical support",
    "Value delivered by AI-powered predictive analytics",
    "Reliability and performance of cloud infrastructure",
    "Flexibility of pricing and contract terms",
])

rpt.page_break()

# -----------------------------------------------------------------------------
# PAGE 6: PROJECT PORTFOLIO
# -----------------------------------------------------------------------------
rpt.title_block("Strategic Initiatives", subtitle="Project Portfolio Status")

rpt.section(
    "Major Projects",
    "The company is executing four strategic initiatives totaling $22.2M in investment. "
    "Overall portfolio health is good with 50% of projects on track. The Security "
    "Overhaul project requires attention due to vendor delays, though mitigation "
    "strategies are in place.",
)

rpt.table("Active Projects", projects, caption="Strategic project portfolio status and budget tracking.")

rpt.spacer()

rpt.section(
    "Project Details",
    "",
    subheading="Platform 2.0 Migration (65% Complete)",
)

rpt.section(
    "",
    "The core infrastructure modernization is progressing well with database migration "
    "completed and API layer 80% refactored. Performance improvements of 40% have already "
    "been observed in early production deployments. Expected completion: December 2025.",
)

rpt.section(
    "",
    "",
    subheading="AI Analytics Suite (100% Complete ✓)",
)

rpt.section(
    "",
    "Successfully launched ahead of schedule with strong market reception. The suite "
    "includes predictive churn modeling, revenue forecasting, and natural language "
    "querying capabilities. Early adopters report 25% improvement in decision-making speed.",
)

rpt.page_break()

# -----------------------------------------------------------------------------
# PAGE 7: RISK MANAGEMENT
# -----------------------------------------------------------------------------
rpt.title_block("Risk Management", subtitle="Risk Assessment & Mitigation")

rpt.section(
    "Risk Overview",
    "The Risk Committee has identified and is actively managing five key enterprise "
    "risks. Overall risk profile remains stable with no critical risks requiring "
    "immediate board intervention. The cybersecurity risk has been elevated to High "
    "priority following industry-wide threat intelligence.",
)

rpt.table("Risk Register", risk_register, caption="Active risk register with mitigation status.")

rpt.spacer()

rpt.bullets("Mitigation Strategies", [
    "<b>Vendor Risk:</b> Multi-cloud deployment 70% complete; no single vendor exceeds 40% of workload",
    "<b>Personnel Risk:</b> Key person insurance in place; succession plans documented for all VPs",
    "<b>Security Risk:</b> $6M security overhaul underway; 24/7 SOC operational; quarterly penetration testing",
    "<b>Economic Risk:</b> Client diversification with no single customer >15% of revenue",
    "<b>Compliance Risk:</b> External audit scheduled; legal team expanded with compliance specialist",
])

rpt.page_break()

# -----------------------------------------------------------------------------
# PAGE 8: ORGANIZATION & TEAM
# -----------------------------------------------------------------------------
rpt.title_block("Organization & Talent", subtitle="Team Structure & Growth")

rpt.section(
    "Headcount Overview",
    "Total headcount reached 290 employees across six departments. Q3 saw net addition "
    "of 27 team members with engineering hiring prioritized. The company maintains a "
    "healthy 4.3/5.0 employee satisfaction score with voluntary turnover at 8% (industry "
    "average: 13%).",
)

rpt.table("Team Structure", teams, caption="Department breakdown and hiring metrics.")

rpt.spacer()

rpt.section(
    "Talent Acquisition",
    "Hiring velocity increased in Q3 with 27 new hires and 20 open positions. "
    "Engineering remains the priority with 8 active requisitions for senior roles. "
    "Time-to-hire improved to 34 days from 42 days in Q2.",
)

rpt.bullets("Key Hires in Q3", [
    "Chief Information Security Officer (ex-Fortune 100)",
    "VP of International Sales (15 years APAC enterprise experience)",
    "Principal AI/ML Engineer (PhD, ex-Google Research)",
    "Director of Customer Success (led team scaling at SaaS unicorn)",
    "12 senior software engineers across platform and infrastructure teams",
])

rpt.bullets("Employee Development", [
    "Leadership training program launched for 45 high-potential employees",
    "Technical certification program: 67 employees completed AWS/Azure certs",
    "Mentorship program pairing 89 junior employees with senior leaders",
    "Quarterly all-hands with 94% attendance and 4.5/5.0 satisfaction rating",
])

rpt.page_break()

# -----------------------------------------------------------------------------
# PAGE 9: MILESTONES & TIMELINE
# -----------------------------------------------------------------------------
rpt.title_block("Milestones & Roadmap", subtitle="Achievements & Upcoming Deliverables")

rpt.section(
    "Quarterly Milestones",
    "Q3 delivered two major milestones ahead of schedule. The Series C funding and "
    "AI Analytics Suite launch represent significant strategic achievements. Q4 will "
    "focus on security certification, international expansion, and mobile platform "
    "modernization.",
)

rpt.table("Milestone Tracker", milestones, caption="Q3 achievements and Q4 planned milestones.")

rpt.spacer()

rpt.section(
    "Strategic Roadmap",
    "",
    subheading="Q4 2025 Priorities",
)

rpt.bullets("", [
    "Complete SOC 2 Type II audit and achieve certification",
    "Open Singapore office and hire initial APAC team (target: 5 employees)",
    "Launch Mobile App v3.0 with offline capabilities and improved UX",
    "Achieve $140M revenue run-rate by year-end",
    "Expand Enterprise Sales team to support Fortune 500 acquisition",
])

rpt.section(
    "",
    "",
    subheading="2026 Strategic Objectives",
)

rpt.bullets("", [
    "Reach $200M ARR with 30% year-over-year growth maintained",
    "Expand international revenue to 25% of total (from current 8%)",
    "Launch Partner Channel program targeting 15% of new revenue",
    "Achieve GAAP profitability by Q2 2026",
    "Complete Series D funding at $1.5B+ valuation",
])

rpt.page_break()

# -----------------------------------------------------------------------------
# PAGE 10: CONCLUSION & NEXT STEPS
# -----------------------------------------------------------------------------
rpt.title_block("Conclusion", subtitle="Summary & Forward Outlook")

rpt.section(
    "Quarter in Review",
    "Q3 2025 represents a transformational quarter for {company}. The combination of "
    "strong financial performance, successful product launches, and strategic funding "
    "positions the company for accelerated growth. We have proven the viability of our "
    "AI-first strategy and established product-market fit across all customer segments."
    "<br/><br/>"
    "The disciplined execution of our strategic roadmap, combined with exceptional "
    "talent acquisition and retention, creates a foundation for sustained market "
    "leadership. Our focus on customer success is reflected in industry-leading NPS "
    "scores and near-zero enterprise churn."
    "<br/><br/>"
    "As we enter Q4, the organization is aligned on three priorities: achieving "
    "security certifications, expanding into APAC, and preparing for our next growth "
    "phase. With $125M in cash reserves and a clear path to profitability, we are "
    "well-positioned to navigate any market uncertainties while capturing the "
    "significant opportunity ahead.".format(company=COMPANY_NAME),
)

rpt.spacer()

rpt.section("Immediate Actions", "")

rpt.bullets("Board Decisions Required", [
    "Approve $8M additional security investment to accelerate certification timeline",
    "Authorize Singapore entity formation and initial $2M APAC market entry budget",
    "Review and approve 2026 operating plan and budget allocation",
    "Evaluate acquisition opportunity: preliminary due diligence on $50M revenue target",
])

rpt.bullets("Executive Team Actions", [
    "Complete CISO onboarding and security roadmap presentation to board (Oct 25)",
    "Finalize APAC leadership hiring and office location selection (Oct 30)",
    "Present Q4 revenue forecast refinement based on strong pipeline (Nov 5)",
    "Conduct quarterly talent review and succession planning updates (Nov 15)",
])

rpt.spacer(15)

rpt.section(
    "",
    "<i>This report was prepared by the Office of the Chief Executive in collaboration "
    "with the Finance, Product, and Operations teams. For questions or additional "
    "information, please contact the Executive Assistant to the CEO.</i>",
)

# =============================================================================
# BUILD THE REPORT
# =============================================================================

rpt.build()

print("✓ Report generated: quarterly_business_review_q3_2025.pdf")
print(f"✓ {COMPANY_NAME} {REPORT_TITLE}")
print(f"✓ Period: {REPORT_PERIOD}")
print(f"✓ Generated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}")
