
import unittest
from mock import MagicMock
import allensdk.core.json_utilities as ju
from allensdk.api.queries.rma_cookbook import RmaCookbook

class ApiCookbookTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ApiCookbookTests, self).__init__(*args, **kwargs)
        self.cookbook = None
    
    
    def setUp(self):
        self.cookbook = \
            {"ontology_queries": [
                {'name': 'structures_by_graph_ids',
                 'description': 'see name',
                 'model': 'Structure',
                 'criteria': '[graph_id$in%s]',
                 'order': ['structures.graph_order'],
                 'num_rows': 'all',
                 'count': False,
                 'criteria_params': ['graph_ids']
                },
                {'name': 'structures_by_graph_names',
                 'description': 'see name',
                 'model': 'Structure',
                 'criteria': 'graph[structure_graphs.name$in%s]',
                 'order': ['structures.graph_order'],
                 'num_rows': 'all',
                 'count': False,
                 'criteria_params': ['graph_names']
                },
                {'name': 'structures_by_set_ids',
                 'description': 'see name',
                 'model': 'Structure',
                 'criteria': '[structure_set_id$in%s]',
                 'order': ['structures.graph_order'],
                 'num_rows': 'all',
                 'count': False,
                 'criteria_params': ['set_ids']
                },
                {'name': 'structures_by_set_names',
                 'description': 'see name',
                 'model': 'Structure',
                 'criteria': 'structure_sets[name$in%s]',
                 'order': ['structures.graph_order'],
                 'num_rows': 'all',
                 'count': False,
                 'criteria_params': ['set_names']
                },
                {'name': 'structure_graphs_list',
                 'description': 'see name',
                 'model': 'StructureGraph',
                 'num_rows': 'all',
                 'count': False
                },
                {'name': 'structure_sets_list',
                 'description': 'see name',
                 'model': 'StructureSet',
                 'num_rows': 'all',
                 'count': False
                },
                {'name': 'atlases_list',
                 'description': 'see name',
                 'model': 'Atlas',
                 'num_rows': 'all',
                 'count': False
                },
                {'name': 'atlases_table',
                 'description': 'see name',
                 'model': 'Atlas',
                 'criteria': 'structure_graph(ontology),graphic_group_labels',
                 'include': '[structure_graph(ontology),graphic_group_labels',
                 'order': ['structures.graph_order'],
                 'num_rows': 'all',
                 'count': False
                },
                {'name': 'atlases_table_brief',
                 'description': 'see name',
                 'model': 'Atlas',
                 'criteria': 'structure_graph(ontology),graphic_group_labels',
                 'include': 'structure_graph(ontology),graphic_group_labels',
                 'order': ['structures.graph_order'],
                 'only': ['atlases.id',
                           'atlases.name',
                           'atlases.image_type',
                           'ontologies.id',
                           'ontologies.name',
                           'structure_graphs.id',
                           'structure_graphs.name',
                           'graphic_group_labels.id',
                           'graphic_group_labels.name'],
                 'num_rows': 'all',
                 'count': False
                }
            ]}
        self.rma = RmaCookbook(query_manifest=self.cookbook)
    
    
    def tearDown(self):
        self.rma= None
        self.cookbook = None
        
    
    def test_atlases_list(self):
        ju.read_url_get = \
            MagicMock(name='read_url_get',
                      return_value={ 'msg': [{ 'whatever': True }] })
        
        self.rma.cookbook_query('ontology_queries',
                                'atlases_list')
        
        ju.read_url_get.assert_called_once_with('http://api.brain-map.org/api/v2/data/query.json?q=model::Atlas,rma::options%5Bnum_rows$eq%27all%27%5D%5Bcount$eqfalse%5D')
    
    
    def test_structure_graphs_list(self):
        ju.read_url_get = \
            MagicMock(name='read_url_get',
                      return_value={ 'msg': [{ 'whatever': True }] })
        
        self.rma.cookbook_query('ontology_queries',
                                'structure_graphs_list')
        
        ju.read_url_get.assert_called_once_with('http://api.brain-map.org/api/v2/data/query.json?q=model::StructureGraph,rma::options%5Bnum_rows$eq%27all%27%5D%5Bcount$eqfalse%5D')
    
    
    def test_structure_sets_list(self):
        ju.read_url_get = \
            MagicMock(name='read_url_get',
                      return_value={ 'msg': [{ 'whatever': True }] })
        
        self.rma.cookbook_query('ontology_queries',
                                'structure_sets_list')
        
        ju.read_url_get.assert_called_once_with('http://api.brain-map.org/api/v2/data/query.json?q=model::StructureSet,rma::options%5Bnum_rows$eq%27all%27%5D%5Bcount$eqfalse%5D')
    
    
    def test_structures_by_graph_ids(self):
        ju.read_url_get = \
            MagicMock(name='read_url_get',
                      return_value={ 'msg': [{ 'whatever': True }] })
        
        self.rma.cookbook_query('ontology_queries',
                                'structures_by_graph_ids',
                                graph_ids='1')
        
        ju.read_url_get.assert_called_once_with('http://api.brain-map.org/api/v2/data/query.json?q=model::Structure,rma::criteria,%5Bgraph_id$in1%5D,rma::options%5Bnum_rows$eq%27all%27%5D%5Bcount$eqfalse%5D')
    
    
    def test_structures_by_graph_names(self):
        ju.read_url_get = \
            MagicMock(name='read_url_get',
                      return_value={ 'msg': [{ 'whatever': True }] })
        
        self.rma.cookbook_query('ontology_queries',
                                'structures_by_graph_names',
                                graph_names=self.rma.quote_string('Human+Brain+Atlas'))
        
        ju.read_url_get.assert_called_once_with('http://api.brain-map.org/api/v2/data/query.json?q=model::Structure,rma::criteria,graph%5Bstructure_graphs.name$in%27Human+Brain+Atlas%27%5D,rma::options%5Bnum_rows$eq%27all%27%5D%5Bcount$eqfalse%5D')
    
    
    def test_structures_by_set_ids(self):
        ju.read_url_get = \
            MagicMock(name='read_url_get',
                      return_value={ 'msg': [{ 'whatever': True }] })
        
        self.rma.cookbook_query('ontology_queries',
                                'structures_by_graph_ids',
                                graph_ids='1')
        
        ju.read_url_get.assert_called_once_with('http://api.brain-map.org/api/v2/data/query.json?q=model::Structure,rma::criteria,%5Bgraph_id$in1%5D,rma::options%5Bnum_rows$eq%27all%27%5D%5Bcount$eqfalse%5D')
    
    
    def test_atlases_table(self):
        ju.read_url_get = \
            MagicMock(name='read_url_get',
                      return_value={ 'msg': [{ 'whatever': True }] })
        
        self.rma.cookbook_query('ontology_queries',
                                'atlases_table')
        
        ju.read_url_get.assert_called_once_with('http://api.brain-map.org/api/v2/data/query.json?q=model::Atlas,rma::criteria,structure_graph%28ontology%29,graphic_group_labels,rma::include,%5Bstructure_graph%28ontology%29,graphic_group_labels,rma::options%5Bnum_rows$eq%27all%27%5D%5Bcount$eqfalse%5D')
    
    
    def test_atlases_table_brief(self):
        ju.read_url_get = \
            MagicMock(name='read_url_get',
                      return_value={ 'msg': [{ 'whatever': True }] })
        
        self.rma.cookbook_query('ontology_queries',
                                'atlases_table_brief')
        
        ju.read_url_get.assert_called_once_with('http://api.brain-map.org/api/v2/data/query.json?q=model::Atlas,rma::criteria,structure_graph%28ontology%29,graphic_group_labels,rma::include,structure_graph%28ontology%29,graphic_group_labels,rma::options%5Bonly$eqatlases.id,atlases.name,atlases.image_type,ontologies.id,ontologies.name,structure_graphs.id,structure_graphs.name,graphic_group_labels.id,graphic_group_labels.name%5D%5Bnum_rows$eq%27all%27%5D%5Bcount$eqfalse%5D')
