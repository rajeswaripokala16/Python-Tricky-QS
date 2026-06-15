from pdf2pptx import Converter

# Convert PDF to PPT
cv = Converter("68aaf1612c6ca_Hackshastra_ppt.pdf")
cv.convert("68aaf1612c6ca_Hackshastra_ppt.pptx")
cv.close()
