<!DOCTYPE html>

<!DOCTYPE html>
<html>
<head>
<title>Admin Console</title>
</head>
<body>

%if username != None:
Welcome {{username}}	<a href="/logout">Logout</a>
%end
 | <a href="/">Home</a>

<h1>Admin Console</h1>

Signups Status: {{prefs.get('signups', "None")}} | <a href="/pref/set/signups/enabled">Enable</a> | <a href="/pref/set/signups/disabled">Disable</a><br /><br />
Users:<br />
<table>
	%for user in users:
	<td>{{user['name']}}</td><td>{{user['email']}}</td><td>{{str(user['roles'])}}</td>
	%end
</table>
<br /><br />
Create User:
<form action="/signup" method="POST">
	<table>
		<tr><td>Username: </td><td><input type="text" name="username"/></td></tr>
		<tr><td>Email Address: </td><td><input type="text" name="email"/></td></tr>
		<tr><td>Password: </td><td><input type="password" name="password"/></td></tr>
		<tr><td>Verify Password:</td><td><input type="password" name="verify"/></td></tr>
	</table>
	<input type="submit" />
</form>

</body>
</html>