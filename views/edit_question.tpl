<!DOCTYPE html>

<!DOCTYPE html>
<html>
<head>
<title>Edit Question</title>
</head>
<body>

%if username != None:
Welcome {{username}}	<a href="/logout">Logout</a>
%end
 | <a href="/">Home</a>

<br />{{errors}}

<h1>Edit Question</h1>
<a href="{{back_link}}">Back to Test</a>
<form action = "/question/{{question_id}}" method="POST">
	<input type="hidden" name="back_link" value="{{back_link}}" />
	<input type="hidden" name="_id" value="question_id" />
	<h2>Topic</h2>
	<select name="topic">
		<option value="new">New Topic</option>
		%for topic in topics:
			%if topic == selected_topic:
				<option value="{{topic}}" selected>{{topic}}</option>
			%else:
				<option value="{{topic}}">{{topic}}</option>
			%end
		%end
	</select>
	<br />New Topic: <input type="text" name="new_topic" value="{{new_topic}}"></input>
	<h2>Question</h2>
	<textarea name="question" cols="80" rows="10">{{question}}</textarea>
	<br />Image URLs: <input type="text" name="image_urls" value="{{', '.join(image_urls)}}" /> e.g. http://url1.com/image.png, http://url2.com/image2.png
	<h2>Answer</h2>
	<textarea name="answer" cols="80" rows="10">{{answer}}</textarea>
	<br />Levels: 
	%for level in [1,2,3]:
		%if str(level) in levels:
			<input type="checkbox" name="level" value="{{level}}" checked />L{{level}}
		%else:
			<input type="checkbox" name="level" value="{{level}}" />L{{level}}
		%end
	%end
	<br /><input type="Submit" />

</form>

</body>
</html>
