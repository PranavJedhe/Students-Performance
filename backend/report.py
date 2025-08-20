from flask import Blueprint, send_file, jsonify
from io import BytesIO
from fpdf import FPDF
from rank_analytics import SAMPLE_RANKINGS

report_bp = Blueprint('report', __name__)

@report_bp.route('/api/report')
def report_root():
    """Root endpoint for the Report module."""
    return jsonify(module='Report module')


@report_bp.route('/api/report/export')
def export_report():
    """Generate a simple PDF with ranking data and send it."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Student Rankings", ln=True)
    for r in SAMPLE_RANKINGS:
        pdf.cell(0, 10, f"{r['rank']}. {r['student']} - GPA {r['gpa']}", ln=True)
    pdf_bytes = pdf.output(dest="S").encode("latin1")
    pdf_buffer = BytesIO(pdf_bytes)
    return send_file(
        pdf_buffer,
        mimetype="application/pdf",
        as_attachment=True,
        download_name="report.pdf",
    )
