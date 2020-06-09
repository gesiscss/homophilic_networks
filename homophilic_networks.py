def explorer(nodes_value=100, new_edges_value=2, minority_value=0.2, homophily_value=0.5):
    
    from generate_homophilic_graph_symmetric import homophilic_ba_graph
    import ipywidgets
    import networkx as nx
    import matplotlib.pyplot as plt
    
    def network(nodes, new_edges, minority, homophily):
        G = homophilic_ba_graph(N=nodes, m=new_edges, minority_fraction=minority, homophily=homophily)
        color = nx.get_node_attributes(G, 'color')
        d = dict(G.degree)
        pos = nx.spring_layout(G, k=0.25)
        plt.figure(figsize=(6, 6))
        nx.draw_networkx_edges(G, pos=pos, alpha=0.4)
        nx.draw_networkx_nodes(
            G, pos=pos, nodelist=color.keys(),
            node_size=[v*15 for v in d.values()],
            node_color=list(color.values()),
            cmap=plt.cm.Reds_r
        )
        plt.axis('off')
        plt.show()
    
    ipywidgets.interact(
        network,
        nodes=ipywidgets.IntSlider(value=nodes_value, min=10, max=200, step=10),
        new_edges=ipywidgets.IntSlider(value=new_edges_value, min=1, max=5, step=1),
        minority=ipywidgets.FloatSlider(value=minority_value, min=0., max=0.5, step=0.1),
        homophily=ipywidgets.FloatSlider(value=homophily_value, min=0., max=1., step=0.1)
    )
