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

Signups Status: {{prefs.get('signups', "None")}} | Enable | Disable<br />
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