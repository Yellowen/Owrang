// Copyright (c) 2013, Web Notes Technologies Pvt. Ltd.
// License: GNU General Public License v3. See license.txt

owrang.fs = {}

pscript['onload_Financial Statements'] = function(wrapper) {
	wn.ui.make_app_page({
		parent: wrapper,
		"title": "Financial Statements",
		"single_column": true,
	});
	
	owrang.fs.stmt_type = wrapper.appframe.add_field({
		fieldtype:"Select",
		fieldname:"stmt_type",
		options: ['Select Statement...','Balance Sheet','Profit & Loss']
	})

	owrang.fs.stmt_company = wrapper.appframe.add_field({
		fieldtype:"Select",
		fieldname:"stmt_company",
		options: ['Loading Companies...']
	})

	owrang.fs.stmt_period = wrapper.appframe.add_field({
		fieldtype:"Select",
		fieldname:"stmt_period",
		options: ['Select Period...', 'Annual', 'Quarterly', 'Monthly']
	})

	owrang.fs.stmt_fiscal_year = wrapper.appframe.add_field({
		fieldtype:"Select",
		fieldname:"stmt_fiscal_year",
		options: ['Loading...']
	})

	wrapper.appframe.add_button("Create", function() {
		pscript.stmt_new();
	}, "icon-refresh")

	wrapper.appframe.add_button("Print", function() {
		_p.go($i('print_html').innerHTML);
	}, "icon-print")
		
	$(wrapper).find(".layout-main").html('<div id="print_html">\
		<div id="stmt_title1" style="margin:16px 0px 4px 0px; font-size: 16px; font-weight: bold; color: #888;"></div>\
		<div id="stmt_title2" style="margin:0px 0px 8px 0px; font-size: 16px; font-weight: bold;"></div>\
		<div id="stmt_tree" style="margin: 0px 0px 16px; overflow: auto;">Please select options and click on Create</div>\
	</div>').css({"min-height": "400px"});

  // load companies
  return $c_obj('MIS Control','get_comp','', function(r,rt) {    
    // company
	owrang.fs.stmt_company.$input.empty()
		.add_options(['Select Company...'].concat(r.message.company));
	owrang.fs.stmt_fiscal_year.$input.empty()
		.add_options(['Select Year...'].concat(r.message.fiscal_year));
  });

}

pscript.stmt_new = function(stmt,company_name,level,period,year) {
    
  $i('stmt_tree').innerHTML = 'Refreshing....';
  $i('stmt_tree').style.display = 'block';
  
  var company =owrang.fs.stmt_company.get_value();

  var arg = {
  	statement: owrang.fs.stmt_type.get_value(),
  	company: company,
  	period: owrang.fs.stmt_period.get_value(),
  	year: owrang.fs.stmt_fiscal_year.get_value()
  }

  return $c_obj('MIS Control', 'get_statement', docstring(arg), function(r,rt) {
      var nl = r.message;
      var t = $i('stmt_tree');
      var stmt_type = owrang.fs.stmt_type.get_value();
      t.innerHTML = '';
      var tab = $a($a(t, 'div'),'table','stmt_table');
      tab.style.tableLayout = 'fixed';
      tab.style.width = '100%';
      
      $i('stmt_title1').innerHTML = owrang.fs.stmt_company.get_value()
      $i('stmt_title2').innerHTML = owrang.fs.stmt_type.get_value() 
		+ ' - ' + owrang.fs.stmt_fiscal_year.get_value();
      for(i=0;i<nl.length;i++) {
        tab.insertRow(i);
        
        tab.rows[i].style.height = '20px';
        
        // heads
        var per = tab.rows[i].insertCell(0);
        per.style.width = '150px';
        per.innerHTML = pscript.space_reqd(nl[i][0])+cstr(nl[i][1]);
        per.className = 'stmt_level' + nl[i][0];
        
        // Make Title Bold
        if(nl[i][0] == 0 || nl[i][0] == 1 || nl[i][0] == 4){
          per.innerHTML = (pscript.space_reqd(nl[i][0])+cstr(nl[i][1])+'').bold();
          per.style.fontSize = '12px';
        }

        for(j=2;j<nl[i].length;j++){
          var per = tab.rows[i].insertCell(j-1);
//          per.style.width = (100-acc_width)/(nl[i].length-2) +'%';
          per.style.width = '150px';
          per.style.textAlign = "right";
          per.className = 'stmt_level' + nl[i][0];
          if (i==0) {
            per.style.fontSize = '14px';
            per.style.textAlign = "right";
          }
          if (nl[i][0]==5) {
            if(flt(nl[i][j])<0.0) per.style.color = "RED";
            else per.style.color = "GREEN";
          }
          if(nl[i][0] != 0){
            if(nl[i][j]) {
              if (i==0) 
				per.innerHTML = (nl[i][j]+'').bold();
              else if(nl[i][0] == 1 || nl[i][0] == 4) 
				per.innerHTML = format_currency(nl[i][j], owrang.get_currency(company)).bold();
              else 
				per.innerHTML = format_currency(nl[i][j], owrang.get_currency(company))
            } else
              per.innerHTML = '-';
          }
        }
      }
    
  });	
  $i('stmt_tree').style.display = 'block';  
}

//printing statement
pscript.print_statement = function(){
  print_go($i('print_html').innerHTML);
}

//determine space to be given
pscript.space_reqd = function(val){
  if(val == 1) return '  ';
  else if(val == 2) return '     ';
  else if(val == 3) return '        ';
  else return '';  
}