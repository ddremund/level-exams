<!DOCTYPE html>

<!DOCTYPE html>
<html>
<head>
<title>Create Custom Test</title>
</head>
<body>

%if username != None:
Welcome {{username}}	<a href="/logout">Logout</a>
%end
<a href="/">Home</a>

<br />{{errors}}

<h1>Create Custom Test</h1>
<form action = "/test/custom" method="POST">
	<h2>Target Level</h2>
	<select name="dest_level">
		%for level in [1,2,3]:
			%if level == selected_level:
				<option value="{{level}}" selected>{{level}}</option>
			%else:
				<option value="{{level}}">{{level}}></option>
			%end
		%end
	</select>
	<h2>Description: </h2><input type="text" name="name" />
	<h2>Percentage of questions to take from level minus one: </h2><input type="text" name="pct_lower_level" />
	<h2>Question Counts</h2>
	<table>
		%for topic in topics:
		<tr><td>{{topic}}:</td><td><input type="text" name="{{topic}}"</td></tr>
	</table>
	<br /><input type="submit" />
</form>

</body>
</html>