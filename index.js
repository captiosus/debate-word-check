var w = 500, h = 500;
var r = 100;

var color = function(i){
    if (i == 0){ //Color for bernie
	return "#9999FF";
    } else if (i == 1){ //Color for hillary
	return "#FF8888";
    } else { //Otherwise default to black
	return "#000000";
    }
};

data = [{"label":"Bernie", "value":30}, 
        {"label":"Hillary", "value":70}];

var savage = d3.select("body")
        .append("svg:svg")              
        .data([data])                   
            .attr("width", w)           
            .attr("height", h)
        .append("svg:g")                
            .attr("transform", "translate(" + r + "," + r + ")");   

var arc = d3.svg.arc()              
    .outerRadius(r);

var pie = d3.layout.pie()          
    .value(function(d) { return d.value; });    

var arcs = savage.selectAll("g.slice")    
    .data(pie)                          
    .enter()                            
      .append("svg:g")                
        .attr("class", "slice");    

    arcs.append("svg:path")
      .attr("fill", function(d, i) { return color(i); } ) 
      .attr("d", arc);    
                                
    arcs.append("svg:text")                                     
      .attr("transform", function(d) {                    
          d.innerRadius = 0;
          d.outerRadius = r;
          return "translate(" + arc.centroid(d) + ")";        
      })
      .attr("text-anchor", "middle")                          
      .text(function(d, i) { return data[i].label; });        
