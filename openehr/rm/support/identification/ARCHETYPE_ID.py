__author__ = 'chrispess'


from openehr.rm.support.identification import OBJECT_ID

class ARCHETYPE_ID(OBJECT_ID):

#referência, globalmente, uma entidade do modelo.
# ex
 qualifiedRmEntity = str()


#organizaão de onde se origina o modelo de referência base do arquétipo.
#ex: "openehr", "cen", "hl7"
rmOriginator = str()

#nome do modelo de referência.
# ex: "en13606", "ehr_rm"
rmName = str()



#nome do nível ontológico do modelo de referência do qual o arquétipo se origina.
# ex: "section", "entry", "folder", "composition"
rmEntity = str()

#nomedoconceito representado pelo arquétipo, incluindo especializações.
# ex: "biochemistry_result-cholesterol"
domainConcept = str()

#nome da especialização do conceito, se o arquétipo for a especialização
# de outro arquétipo. ex: "cholesterol"
specialization = str()


#vesão do arquétipo
versionID = str()

