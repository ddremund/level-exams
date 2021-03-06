<!DOCTYPE html>

<!DOCTYPE html>
<html>
<head>
<title>Edit Custom Test Template</title>
</head>
<body>

%if username != None:
Welcome {{username}}	<a href="/logout">Logout</a>
%end
 | <a href="/">Home</a>

<br />{{errors}}

<h1>Edit Custom Test Template</h1>
<form action = "/test/custom/{{template_id}}" method="POST">
	<h2>Target Level</h2>
	<select name="dest_level">
		%for level in [1,2,3]:
			%if level == selected_level:
				<option value="{{level}}" selected>{{level}}</option>
			%else:
				<option value="{{level}}">{{level}}</option>
			%end
		%end
	</select>
	<h2>Description: </h2><input type="text" name="name" value="{{name}}"/>
	<h2>Percentage of questions to take from level minus one: </h2><input type="text" name="pct_lower" value="{{pct_lower}}"/>
	<h2>Target Question Counts</h2>
	<table>
		%for topic in topics:
		<tr><td>{{topic}}:</td><td><input type="text" name="{{topic}}" value="{{topic_counts.get(topic, 0)}}"/></td></tr>
		%end
	</table>
	<br /><input type="submit" value="Update Template"/>
</form>

</body>
</html>