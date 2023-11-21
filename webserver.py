<tr>
    <th align="center" bgcolor="yellow">8-10</th>
    <td align="center" bgcolor="cyan" colspan="3">FREE SLOT</td>
    <td align="center" bgcolor="cyan">PHY</td>
    <td align="center" bgcolor="cyan">CHE</td>
</tr>

<tr>
    <th align="center" bgcolor="yellow">10-12</th>
    <td align="center" bgcolor="cyan">GER</td>
    <td align="center" bgcolor="cyan">CHE</td>
</tr>

<tr>
    <th align="center" bgcolor="yellow">10-12</th>
    <td align="center" bgcolor="cyan">GER</td>
    <td align="center" bgcolor="cyan">FREE SLOT</td>
    <td align="center" bgcolor="cyan">FWAD</td>
    <td align="center" bgcolor="cyan">FWAD</td>
    <td align="center" bgcolor="cyan">PHY</td>
</tr>

<tr>
    <th align="center" bgcolor="yellow">12-1</th>
    <td align="center" bgcolor="cyan" colspan="5">LUNCH</td>
</tr>

<tr>
    <th align="center" bgcolor="yellow">1-3</th>
    <td align="center" bgcolor="cyan" colspan="2">FREE SLOT</td>
    <td align="center" bgcolor="cyan">MAT</td>
    <td align="center" bgcolor="cyan">MAT</td>
    <td align="center" bgcolor="cyan">SS</td>
</tr>

<tr>
    <th align="center" bgcolor="yellow">3-5</th>
    <td align="center" bgcolor="cyan" colspan="2">FREE SLOT</td>
    <td align="center" bgcolor="cyan">GER</td>
    <td align="center" bgcolor="cyan">CHE</td>
    <td align="center" bgcolor="cyan">FWAD</td>
</tr>
</table>

<table border="3" width="600" cellspacing='3' cellpaddling='3'>

<tr>
    <th align="center">S.No</th>
    <th align="center">SUBJECT CODE</th> 
    <th align="center">Subject Name</th>
</tr>

<tr>
    <td align="center">1</td>
    <td align="center">19A1414</td>
    <td align="centre">Fundamentals of Web Application Devlopment(FWAD)</td>
</tr>

<tr>
    <td align="center">2</td>
    <td align="center">19EN612</td>
    <td align="centre">German Basics (GER)</td>
</tr>

<tr>
    <td align="center">3</td>
    <td align="center">19PH206</td>
    <td align="centre">Physics for Information Technology</td>
</tr>

<tr>
    <td align="center">4</td> 
    <td align="center">19CY205</td>
    <td align="centre">Principles of Chemistry in Engineering(CHE)</td>
</tr>

<tr>
    <td align="center">5</td>
    <td align="center">19MA201</td>
    <td align="centre">Calculus and Matrix Algebra (MAT)</td>
</tr>

<tr>
    <td align="center">6</td>
    <td align="center">19EY701</td>
    <td align="center">soft skills(SS)</td>
    </tr>


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()