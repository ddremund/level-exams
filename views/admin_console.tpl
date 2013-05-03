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
 
 <br />{{errors}}

<h1>Admin Console</h1>

<b>Signups Status: {{prefs.get('signups', "None")}}</b> | <a href="/pref/set/signups/enabled">Enable</a> | <a href="/pref/set/signups/disabled">Disable</a><br /><br />
<form action="/admin" method="POST">
<table>
	<tr><th>Username</th><th>Email</th>
	%for role in prefs['roles']:
	<th>{{role}}</th>
	%end
	</tr>
	%for user in users:
	<tr><td>{{user['_id']}}</td><td>{{user.get('email', "None provided")}}</td>
		%for role in prefs['roles']:
			%if role in user['roles']:
			<td><input type="checkbox" name="{{user['_id']}}" value="{{role}}" checked/></td>
			%else:
			<td><input type="checkbox" name="{{user['_id']}}" value="{{role}}" /></td>
			%end
		%end
	</tr>
	%end
</table>
<input type="submit" value="Update Roles" />
</form>
<br /><br />
<b>Create User:</b>
<form action="/signup" method="POST">
	<table>
		<tr><td>Username: </td><td><input type="text" name="username"/></td></tr>
		<tr><td>Email Address: </td><td><input type="text" name="email"/></td></tr>
		<tr><td>Password: </td><td><input type="password" name="password"/></td></tr>
		<tr><td>Verify Password:</td><td><input type="password" name="verify"/></td></tr>
	</table>
	<input type="submit" value="Create User"/>
</form>
<br /><br />
<b>Reset Password:</b>
<form action="/admin/reset_password" method="POST">
	Username: 
	<select name="username">
		%for user in users:
		<option value="{{user}}" />
		%end
	</select>
	Password: <input type="password" name="password" /><br />
	<input type="submit" value="Change Password" />
</form>

</body>
</html>