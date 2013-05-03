<!DOCTYPE html>

<!DOCTYPE html>
<html>
<head>
<title>Leveling Test: {{description}}</title>
</head>
<body>

%if username != None:
Welcome {{username}}	<a href="/logout">Logout</a>
%end
 | <a href="/">Home</a>

<h1>Enterprise Windows Leveling Test</h1><br />
Test Template: {{description}}<br />
Generated by: {{username}}<br />
Timestamp: {{timestamp}}<br />
Level to Attain: {{level}}<br />
Percentage of questions at top level: {{pct_top}}<br />
Test permalink: <a href="/test/saved/{{test_id}}">http://leveling.rstnt.com/test/saved/{{test_id}}</a><br />
Candidate Name:<br />
<br /><br />

<table>
	<tr align="left"><th>Topic</th><th>Questions</th></tr>
	%for topic in sorted_topics:
	<tr><td>{{topic}}</td><td>{{len(questions[topic])}}</td></tr>
	%end
	<tr><td>Total</td><td>{{sum(len(q) for q in questions.values())}}</td></tr>
</table>

%for topic in sorted_topics:
<hr />
<h3>{{topic}} - {{len(questions[topic])}} questions</h3>
<ol>
	%for i, question in enumerate(questions[topic]):
	<li><span id="{{topic}}-{{i + 1}}"><b>Q:</b> [Level {{'/'.join(question['levels'])}}] {{!"<br />".join(question['question'].split('\n'))}}</span><br />
	%if len(question['image_urls']) > 0:
	Image URLs: {{!'<a href="#{}-image-{}">{}</a> '.format(topic, i + 1, url)  for url in question['image_urls']}}<br />
	%end
	<br /><b>A:</b> {{!"<br />".join(question['answer'].split('\n'))}}<br /><a href="/question/{{question['_id']}}">Edit Question</a> | <a href="/question/remove/{{question['_id']}}">Delete Question from Database</a><br /><b>Notes:</b> <br /><br /><br /><br /><br /></li>
	%end
</ol>
%end

<hr />
<br />
Images:<br /><br />
%for topic in sorted_topics:
	%for i, question in enumerate(questions[topic]):
		%for j, url in enumerate(question["image_urls"]):
			<span id="{{topic}}-image-{{i + 1}}">Image {{j + 1}} for <a href="#{{topic}}-{{i + 1}}">{{topic}} question #{{i + 1}}</a>: {{url}}</span><br /><br />
			<img src="{{!url}}" /><br /><br /><br />
		%end
	%end
%end

</body>
</html>
