'''
Created on Nov 23, 2018

@author: marif
'''
import sys

import xml.etree.cElementTree as ET
from nose.plugins import attrib

def parse_ct(example, ct):
           
    for node in example:
        if node.tag == 'Node':
#            print(node.attrib['name'])
#            ct.append([]) 
            ct.append(node.attrib['name'])
            parse_ct(node, ct)
        if node.tag == 'Stream':
        #    if node.attrib['class'] == 'input' or node.attrib['class'] == 'output':
#            print(node.attrib['name'],node.attrib['type'])
            ct.append(node.attrib['name'])
            ct.append(node.attrib['type'])
            if node.attrib['class'] == 'input' or node.attrib['class'] == 'output' :
                parse_ct(node, ct)
        if node.tag == 'Value':
#            print(node.attrib['instant'],node.text)
            ct.append(node.attrib['instant'])
            ct.append(node.text)
            parse_ct(node, ct)   
             
    return ct
            
if __name__ == '__main__':
 
    k_file = ''
    
    try:
        k_file = sys.argv[1]
    except IndexError:
        k_file = 'egs/hawk-result-1.xml'        
 
    tree = ET.ElementTree(file=k_file)
    root = tree.getroot()
    
    p_index = 0
    
    result = [] 
    ct = []
    
    for element in tree.iter(tag='Property'):
#        if element.tag == 'name':
        p_name = element.attrib['name']
        result.append([])
#        print(element.attrib['name'])
        result[p_index].append(p_index+1)
        result[p_index].append(p_name)
        for subelem in element:
            if subelem.tag == 'Answer':
                p_status = subelem.text
                result[p_index].append(p_status)
#                print(subelem.attrib['source'], )
                if subelem.text == 'valid':
                    result[p_index].append(True)
                else:
                    result[p_index].append(False)
#                    c_example = subelem.getroot()
                    for celement in element:
                        if celement.tag == 'CounterExample':
                            result[p_index].append(parse_ct(celement,[]))
        
        print(result[p_index])
#        print(ct)
        p_index += 1
        
    pass



