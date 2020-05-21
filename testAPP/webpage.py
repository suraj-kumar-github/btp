#!/usr/bin/env python
# coding: utf-8

# In[1]:



column_names = {
    'num_clients': 'NUMBER OF CLIENTS',
}

data1 = [['a', 'b', 'c', 'd', 'e', 'f'],['g','h','i','j', 'k', 'l'],['m', 'n', 'o', 'p', 'q', 'r']]
    

#tabular format for html
def get_table_data(feature, data, columns, id=''):#(event, data_from_server-rowlists-, column-names, -id-)

    table = """<table id={}>""".format(id)
    #caption
    table+= """<caption>Detect {} """.format(feature)
    table+="""</caption>"""
    
    #table head
    table += """<tr>"""
    for col in columns:#dynamic table columns
        table += '''<th>{}</th>'''.format(column_names.get(col, col).upper())
    table += """</tr>"""
    
    #table body
    for row in data:#data is 2d list now
        table += """<tr>"""
        for i in range(len(columns)):           
                table += """<td>{}</td>""".format(row[i])
        table += """</tr>"""
    table += """</table>"""
    return table




def get_form_data(name, features, id=''):#featureName
    form="""<form id={} name='predict' action="http://localhost:5000/result" method="POST">""".format(id)
    form+="""<fieldset>"""
    form+="""<legend>{}</legend>""".format(name)
    
    form+="""<ul>"""
    for i in range(len(features)):
        val=features[i]
        form+="""<label for={}>{}</label>""".format(val.lower(), val)
        if val.lower()=='country':#country, province, year, month
            form+="""<select id ={} name={}>""".format(val.lower(), val.lower())
            form+="""
                
                <option value="Pakistan">Pakistan</option>
                <option value="China">China</option>
                <option value="Bangladesh">Bangladesh</option>
                <option value="Afganistan">Afganistan</option>
                <option value="India" selected>India</option>
                
            """
        elif val.lower()=='event':#country, province, year, month
            form+="""<select id ={} name={}>""".format(val.lower(), val.lower())
            form+="""
                <option value="Civil unrest">Civil unrest</option>
                <option value="Attack">Attack</option>
                <option value="Disease outbreak">Disease outbreak</option>
                <option value="Flood" selected>Flood</option>
                
            """
        elif val.lower()=='month':#country, province, year, month
            form+="""<select id ={} name={}>""".format(val.lower(), val.lower())
            form+="""
                <option value="January" selected>January</option>
                <option value="February">February</option>
                <option value="March">March</option>
                <option value="April">April</option>
                <option value="May">May</option>
                <option value="June">June</option>
                <option value="July">July</option>
                <option value="August">August</option>
                <option value="September">September</option>
                <option value="October">October</option>
                <option value="November">November</option>
                <option value="December">December</option>
                
            """
        
        elif val.lower()=="state/province":
            form+="""<select id ={} name={}>""".format(val.lower(), val.lower())
            form+="""
                <option value="Punjab" selected>Punjab</option>
                <option value="Sindh">Sindh</option>
                <option value="Balochistan">Balochistan</option>
                <option value="Khyber Pakhtunkhwa">Khyber Pakhtunkhwa</option>
                <option value="Gilgit Baltistan">Gilgit Baltistan</option>
                <option value="Azad Kashmir">Azad Kashmir</option>
                <option value="Islamabad">Islamabad</option>
                
                
                <option value="Qinghai">Qinghai</option>
                <option value="Sichuan">Sichuan</option>
                <option value="Gansu">Gansu</option>
                <option value="Heilongjiang">Heilongjiang</option>      
                <option value="Yunnan">Yunnan</option>
                
                <option value="Hunan">Hunan</option>
                <option value="Shaanxi">Shaanxi</option>
                <option value="Hebei">Hebei</option>
                <option value="Jilin">Jilin</option>
                <option value="Hubei">Hubei</option>
                
                <option value="Guizhou">Guizhou</option>
                <option value="Guangdong">Guangdong</option>
                <option value="Jiangxi">Jiangxi</option>
                <option value="Henan">Henan</option>
                <option value="Shanxi">Shanxi</option>
                
                <option value="Shandong">Shandong</option>
                <option value="Liaoning">Liaoning</option>
                <option value="Anhui">Anhui</option>
                <option value="Fujian">Fujian</option>
                <option value="Jiangsu">Jiangsu</option>
                
                <option value="Zhejiang">Zhejiang</option>
                <option value="Taiwan">Taiwan</option>
                <option value="Hainan">Hainan</option>
                <option value="Hong Kong">Hong Kong</option>
                <option value="Tibet">Tibet</option>
                
                <option value="Beijing">Beijing</option>
                <option value="Xinjiang">Xinjiang</option>
                <option value="Suzhou">Suzhou</option>

                <option value="Andhra Pradesh">Andhra Pradesh</option>
                <option value="Arunachal Pradesh">Arunachal Pradesh</option>
                <option value="Assam">Assam</option>
                <option value="Bihar">Bihar</option>
                <option value="Chhattisgarh">Chhattisgarh</option>
                
                <option value="Goa">Goa</option>
                <option value="Gujarat">Gujarat</option>
                <option value="Haryana">Haryana</option>
                <option value="Himachal Pradesh">Himachal Pradesh</option>
                <option value="Jharkhand">Jharkhand</option>
                
                <option value="Karnataka">Karnataka</option>
                <option value="Kerala">Kerala</option>
                <option value="Madhya Pradesh">Madhya Pradesh</option>
                <option value="Maharashtra">Maharashtra</option>
                <option value="Manipur">Manipur</option>
                
                <option value="Meghalaya">Meghalaya</option>
                <option value="Mizoram">Mizoram</option>
                <option value="Nagaland">Nagaland</option>
                <option value="Odisha">Odisha</option>
                <option value="Punjab">Punjab</option>
                
                <option value="Rajasthan">Rajasthan</option>
                <option value="Sikkim">Sikkim</option>
                <option value="Tamil Nadu">Tamil Nadu</option>
                <option value="Telangana">Telangana</option>
                <option value="Tripura">Tripura</option>
                
                <option value="Uttar Pradesh">Uttar Pradesh</option>
                <option value="Uttarakhand">Uttarakhand</option>
                <option value="West Bengal">West Bengal</option>
                <option value="Andaman">Andaman and Nicobar Islands</option>
                <option value="Chandigarh">Chandigarh</option>
                
                <option value="Dadra">Dadra & Nagar Haveli and Daman & Diu</option>
                <option value="Delhi">Delhi</option>
                <option value="Kashmir">Jammu and Kashmir</option>
                <option value="Lakshadweep">Lakshadweep</option>
                <option value="Puducherry">Puducherry</option>
                
                <option value="Ladakh">Ladakh</option>
                
            """
        elif val.lower()=="year":
            form+="""
            <input type="number" min="2020" max="2030" pattern="[0-9]*" id={} name={}>
            """.format(val.lower(), val.lower())
            
        form+="""</select>"""
    form+="""</ul>"""
    
    
    form+="""</fieldset>"""
    form+="""<input type="submit" value="Predict">"""
    form+="""</form>"""
    form+="""<br>"""
    return form



def get_html_page():
    
    html_template = """
    <!DOCTYPE html>
    <html>
    <meta charset="utf-8">
    <!--[if (gte IE 10)|(gt IEMobile 7)|!(IEMobile)|!(IE)]><!-->
    <meta name="viewport" content="width=device-width">
    
    <head>
        
        <title>Event detection Report</title>
        
        <style>
        body{
            color: #2E2E2E;
            font-family: 'Circular', Avenir, sans-serif;
            background-color: #F2F2F2;
            Margin: 0;
            padding: 0;
            
        }
    
        header{
            margin: 0px;
            padding: 5%;
            text-align: center;
            color:#ffffff;
            background-color: #3c094d;
        }
        table {
          border-collapse: collapse;
          margin: 15px;
        }

        table, td, th {
            
            
            border: 1px solid black;
            min-width: 100px;
            text-align: center;
            

        }
        .bad {
            background-color:#df5f5f;
        }
        .good {
            background-color:#84d984;
        }

        span {
            margin-bottom: 15px;
            font-weight: bold;
        }
        footer{
            background-color:#2E2E2E;
            color:#f2f2f2;
            margin: 10px 0;
            padding:10px;
        }
        
        footer ul{ 
            list-style-type: none; 
        }
        label, input {
            display: block;
        }
        input {
            width: 85%;
            padding: 10px;
            margin-bottom: 15px;
        }

        input:required {
            border-right: 10px solid gray;
        }

        input:optional {
            border-right: 10px solid silver;
        }

        input:focus:invalid {
             border-left: 10px solid red;   
        }

        input:focus:valid {
             border-left: 10px solid green;       
        }

        .nowrap label, .nowrap input {
            display: inline;
            width: auto;
        }
        .nowrap input:optional {
            border: 0;
        }

        textarea {
            width: 90%;
            height: 150px;
        }

        fieldset {
            margin-bottom: 30px;
            background-color: #DDD;
        }

        legend {
            background-color: #DDD;
            padding: 2px 12px;
        }

        input[type=submit] {
            font-size: large;
            width: 100%;
            padding: 15px;
            background-color: yellow;
            margin-top: 25px;
        }
        
        </style>
    </head>
    <body>
        <header>
            <h1>Forecasting Events Via Predictive Analysis</h1>
        </header>
        
        <main>
        <section>
            %FORM_DATA%
        </section>
        <hr>
        <section>
            %TABLE_DATA_EVENT%
        </section>
        </main>
        <hr>
        <footer>
            <nav id>
                <ul>
                    <li>
                        <p>Shubham</p>
                    </li>
                    <li>
                        <p>Saifullah</p>
                    </li>
                    <li>
                        <p>Suraj</p>
                    </li>
                </ul>
            </nav>
        </footer>

    </body>
    </html>
    """

    html_template = html_template.replace('%FORM_DATA%', 
                                         get_form_data
                                        ('Features', ['Country', 'Year', 'Month','Event'], 'form' ) )
    return html_template
    return html_template



def get_html_page_result():
    
    html_template = """
    <!DOCTYPE html>
    <html>
    <meta charset="utf-8">
    <!--[if (gte IE 10)|(gt IEMobile 7)|!(IEMobile)|!(IE)]><!-->
    <meta name="viewport" content="width=device-width">
    
    <head>
        
        <title>Event detection Report</title>
        
        <style>
        body{
            color: #2E2E2E;
            font-family: 'Circular', Avenir, sans-serif;
            background-color: #F2F2F2;
            Margin: 0;
            padding: 0;
            
        }
    
        header{
            margin: 0px;
            padding: 5%;
            text-align: center;
            color:#ffffff;
            background-color: #3c094d;
        }
        table {
          border-collapse: collapse;
          margin: 15px;
          width:device-width;
        }

        table, td, th {
            
            
            border: 1px solid black;
            min-width: 100px;
            text-align: center;
            

        }
        .bad {
            background-color:#df5f5f;
        }
        .good {
            background-color:#84d984;
        }

        span {
            margin-bottom: 15px;
            font-weight: bold;
        }
        footer{
            background-color:#2E2E2E;
            color:#f2f2f2;
            margin: 10px 0;
            padding:10px;
        }
        
        footer ul{ 
            list-style-type: none; 
        }
        label, input {
            display: block;
        }
        input {
            width: 85%;
            padding: 10px;
            margin-bottom: 15px;
        }

        input:required {
            border-right: 10px solid gray;
        }

        input:optional {
            border-right: 10px solid silver;
        }

        input:focus:invalid {
             border-left: 10px solid red;   
        }

        input:focus:valid {
             border-left: 10px solid green;       
        }

        .nowrap label, .nowrap input {
            display: inline;
            width: auto;
        }
        .nowrap input:optional {
            border: 0;
        }

        textarea {
            width: 90%;
            height: 150px;
        }

        fieldset {
            margin-bottom: 30px;
            background-color: #DDD;
        }

        legend {
            background-color: #DDD;
            padding: 2px 12px;
        }

        input[type=submit] {
            font-size: large;
            width: 100%;
            padding: 15px;
            background-color: yellow;
            margin-top: 25px;
        }
        
        </style>
    </head>
    <body>
        <header>
            <h1>Forecasting Events Via Predictive Analysis</h1>
        </header>
        
        <main>
        
        <hr>
        <section>
            %TABLE_DATA_EVENT%
        </section>
        </main>
        <hr>
        <footer>
            <nav id>
                <ul>
                    <li>
                        <p>Shubham</p>
                    </li>
                    <li>
                        <p>Saifullah</p>
                    </li>
                    <li>
                        <p>Suraj</p>
                    </li>
                </ul>
            </nav>
        </footer>

    </body>
    </html>
    """
    html_template = html_template.replace('%TABLE_DATA_EVENT%', 
                                          get_table_data('State/Province',data1, ['Algorithm','Country', 'Year', 'Month','Event', 'State/Province'] ) )
    return html_template
    return html_template




with open("index.html", 'w') as wp:
    wp.write(get_html_page())

with open("t1.html", 'w') as wp2:
    wp2.write(get_html_page_result())