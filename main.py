import re,sys
def entities(t):
 names=re.findall(r'(?<![.!?]\s)(?:\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',t); dates=re.findall(r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b',t); emails=re.findall(r'\b[\w.+-]+@[\w.-]+\b',t)
 return {'names':names,'dates':dates,'emails':emails}
if __name__=='__main__': print(entities(open(sys.argv[1]).read() if len(sys.argv)>1 else input('Text: ')))