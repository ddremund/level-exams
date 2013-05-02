<!DOCTYPE html>

<!DOCTYPE html>
<html>
<head>
<title>Change Password</title>
</head>
<body>

%if username != None:
Welcome {{username}}	<a href="/logout">Logout</a>
%end
<a href="/">Home</a>

<br />{{errors}}<br />
<form action = "/change_password" method="POST">
Change Password: <input type="password" name="new_password" />
<input type="submit" />
</form>

</body>
</html>