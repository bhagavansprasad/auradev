#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <libxml/xmlmemory.h>
#include <libxml/parser.h>

void parseStory (xmlDocPtr doc, xmlNodePtr cur) 
{
	xmlChar *key;

	cur = cur->xmlChildrenNode;

	while (cur != NULL) 
	{
		if (strcmp(cur->name, "text") != 0)
		{
			key = xmlNodeListGetString(doc, cur->xmlChildrenNode, 1);
			printf("-->tag name :%s, value :%s\n", cur->name, key);
			xmlFree(key);
		}

		cur = cur->next;
		continue;

	    if ((!xmlStrcmp(cur->name, (const xmlChar *)"author"))) 
		{
		    key = xmlNodeListGetString(doc, cur->xmlChildrenNode, 1);
		    printf("keyword: %s\n", key);
		    xmlFree(key);
 	    }
		cur = cur->next;
	}
    return;
}

static void parseDoc(char *docname) 
{
	xmlDocPtr doc;
	xmlNodePtr cur;

	doc = xmlParseFile(docname);
	
	if (doc == NULL ) 
	{
		fprintf(stderr,"Document not parsed successfully. \n");
		return;
	}
	
	cur = xmlDocGetRootElement(doc);
	
	if (cur == NULL) 
	{
		fprintf(stderr,"empty document\n");
		xmlFreeDoc(doc);
		return;
	}
	
#if 0
	if (xmlStrcmp(cur->name, (const xmlChar *) "story")) 
	{
		fprintf(stderr,"document of the wrong type, root node != story");
		xmlFreeDoc(doc);
		return;
	}
#endif
	
	cur = cur->xmlChildrenNode;
	while (cur != NULL) 
	{
		//if ((!xmlStrcmp(cur->name, (const xmlChar *)"storyinfo")))
		{
			parseStory (doc, cur);
		}
		 
		cur = cur->next;
	}
	
	xmlFreeDoc(doc);
	return;
}

int main(int argc, char **argv) 
{
	char *docname;
		
	if (argc <= 1) 
	{
		printf("Usage: %s docname\n", argv[0]);
		return(0);
	}

	docname = argv[1];
	parseDoc (docname);
	return (1);
}


