# Confluence Storage Format rules

The protocol is emitted as a Storage Format XML/XHTML fragment.

Required conventions:

- no Markdown fences;
- no XML declaration required;
- no `<html>`, `<head>`, `<body>` wrapper;
- headings preserve the template style;
- tables use `<table class="wrapped">`;
- line breaks inside cells use `<br /><br />`;
- empty values use `<br />`;
- escape XML text characters (`&amp;`, `&lt;`, `&gt;`);
- close every tag;
- keep table row/column counts structurally valid.

Validation may wrap the fragment temporarily in a root element with standard Confluence namespaces. The wrapper is for validation only and must not appear in the returned protocol.
