import re,html
def inline(t):
    t=html.escape(t,quote=False)
    t=re.sub(r'`([^`]+)`',r'<code>\1</code>',t)
    t=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',t)
    t=re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])',r'<em>\1</em>',t)
    return t
def block(text):
    lines=text.splitlines(); out=[]; i=0
    while i<len(lines):
        l=lines[i]
        if l.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                cells=[c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?',c) for c in cells if c): rows.append(cells)
                i+=1
            h='<div class="tbl"><table><thead><tr>'+''.join(f'<th>{inline(c)}</th>' for c in rows[0])+'</tr></thead><tbody>'
            for r in rows[1:]: h+='<tr>'+''.join(f'<td>{inline(c)}</td>' for c in r)+'</tr>'
            out.append(h+'</tbody></table></div>'); continue
        if l.startswith('>'):
            q=[]
            while i<len(lines) and lines[i].startswith('>'):
                q.append(lines[i].lstrip('>').strip()); i+=1
            out.append('<blockquote class="illus">'+''.join(f'<p>{inline(x)}</p>' for x in q if x)+'</blockquote>'); continue
        if re.match(r'^\s*(?:[-*]|\d+\.)\s',l):
            ordered=bool(re.match(r'^\s*\d+\.',l)); items=[]
            while i<len(lines) and (re.match(r'^\s*(?:[-*]|\d+\.)\s',lines[i]) or (lines[i].startswith('  ') and lines[i].strip() and items)):
                if re.match(r'^\s*(?:[-*]|\d+\.)\s',lines[i]) and not lines[i].startswith('  '):
                    items.append(re.sub(r'^\s*(?:[-*]|\d+\.)\s+','',lines[i]))
                else:
                    items[-1]+=' '+re.sub(r'^\s*(?:[-*]|\d+\.)\s+','· ',lines[i].strip())
                i+=1
            tag='ol' if ordered else 'ul'
            out.append(f'<{tag} class="list">' if ordered else '<ul>')
            out[-1]+=''.join(f'<li>{inline(x)}</li>' for x in items)+f'</{tag}>'; continue
        if l.startswith('#'):
            out.append(f'<h4>{inline(l.lstrip("#").strip())}</h4>'); i+=1; continue
        if l.strip() and l.strip()!='---':
            out.append(f'<p>{inline(l.strip())}</p>')
        i+=1
    return '\n'.join(out)
def split(md,level):
    pat=r'^'+'#'*level+r' '
    parts=re.split(pat,md,flags=re.M)
    head=parts[0]; secs=[]
    for p in parts[1:]:
        t,_,b=p.partition('\n'); secs.append((t.strip(),b))
    return head,secs
def card(title,body,code='',defn='',cid=''):
    idattr=f' id="{cid}"' if cid else ''
    c=f'<span class="code">{inline(code)}</span>' if code else ''
    d=f'<span class="def">{inline(defn)}</span>' if defn else ''
    return f'<details class="card"{idattr}><summary>{c}<span class="nm">{inline(title)}</span>{d}</summary><div class="bd">{body}</div></details>'
