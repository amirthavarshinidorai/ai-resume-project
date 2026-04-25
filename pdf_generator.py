from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(filename, skills, score, job_data, feedback):

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("AI Resume Analysis Report", styles['Title']))
    content.append(Spacer(1, 10))

    # Skills
    content.append(Paragraph(f"Skills: {', '.join(skills)}", styles['Normal']))
    content.append(Spacer(1, 10))

    # Score
    content.append(Paragraph(f"Resume Score: {score}%", styles['Normal']))
    content.append(Spacer(1, 10))

    # Jobs
    content.append(Paragraph("Recommended Jobs:", styles['Heading2']))
    for job in job_data:
        content.append(Paragraph(
            f"{job['Job Role']} | Match: {job['Match %']}% | Feasibility: {job['Feasibility']}%",
            styles['Normal']
        ))
        content.append(Spacer(1, 5))

    # Feedback
    content.append(Spacer(1, 10))
    content.append(Paragraph("Resume Suggestions:", styles['Heading2']))

    for f in feedback:
        content.append(Paragraph(f"• {f}", styles['Normal']))

    doc.build(content)