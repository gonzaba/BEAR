# -*- coding: utf-8 -*-
#   Copyright (C) 2011-2012 by
#   Nicholas Mancuso <nick.mancuso@gmail.com>
#   All rights reserved.
#   BSD license.
"""Functions for finding node and edge dominating sets.

A `dominating set`_ for an undirected graph *G* with vertex set *V*
and edge set *E* is a subset *D* of *V* such that every vertex not in
*D* is adjacent to at least one member of *D*. An `edge dominating set`_
is a subset *F* of *E* such that every edge not in *F* is
incident to an endpoint of at least one edge in *F*.

.. _dominating set: https://en.wikipedia.org/wiki/Dominating_set
.. _edge dominating set: https://en.wikipedia.org/wiki/Edge_dominating_set

"""
from __future__ import division

from ..matching import maximal_matching
from ...utils import not_implemented_for

__all__ = ["min_weighted_dominating_set",
           "min_edge_dominating_set"]

__author__ = """Nicholas Mancuso (nick.mancuso@gmail.com)"""


# TODO Why doesn't this algorithm work for directed graphs?
@not_implemented_for('directed')
def min_weighted_dominating_set(G, weight=None):
    """Returns a dominating set that approximates the minimum weight node
    dominating set.

    Parameters
    ----------
    G : NetworkX graph
        Undirected graph.

    weight : string
        The node attribute storing the weight of an node. If provided,
        the node attribute with this key must be a number for each
        node. If not provided, each node is assumed to have weight one.

    Returns
    -------
    min_weight_dominating_set : set
        A set of nodes, the sum of whose weights is no more than `(\log
        w(V)) w(V^*)`, where `w(V)` denotes the sum of the weights of
        each node in the graph and `w(V^*)` denotes the sum of the
        weights of each node in the minimum weight dominating set.

    Notes
    -----
    This algorithm computes an approximate minimum weighted dominating
    set for the graph `G`. The returned solution has weight `(\log
    w(V)) w(V^*)`, where `w(V)` denotes the sum of the weights of each
    node in the graph and `w(V^*)` denotes the sum of the weights of
    each node in the minimum weight dominating set for the graph.

    This implementation of the algorithm runs in $O(m)$ time, where $m$
    is the number of edges in the graph.

    References
    ----------
    .. [1] Vazirani, Vijay V.
           *Approximation Algorithms*.
           Springer Science & Business Media, 2001.

    """
    # The unique dominating set for the null graph is the empty set.
    if len(G) == 0:
        return set()

    # This is the dominating set that will eventually be returned.
    dom_set = set()

    def _cost(node_and_neighborhood):
        """Returns the cost-effectiveness of greedily choosing the given
        node.

        `node_and_neighborhood` is a two-tuple comprising a node and its
        closed neighborhood.

        """
        v, neighborhood = node_and_neighborhood
        return G.nodes[v].get(weight, 1) / len(neighborhood - dom_set)

    # This is a set of all vertices not already covered by the
    # dominating set.
    vertices = set(G)
    # This is a dictionary mapping each node to the closed neighborhood
    # of that node.
    neighborhoods = {v: {v} | set(G[v]) for v in G}

    # Continue until all vertices are adjacent to some node in the
    # dominating set.
    while vertices:
        # Find the most cost-effective node to add, along with its
        # closed neighborhood.
        dom_node, min_set = min(neighborhoods.items(), key=_cost)
        # Add the node to the dominating set and reduce the remaining
        # set of nodes to cover.
        dom_set.add(dom_node)
        del neighborhoods[dom_node]
        vertices -= min_set

    return dom_set


def min_edge_dominating_set(G):
    r"""Return minimum cardinality edge dominating set.

    Parameters
    ----------
    G : NetworkX graph
      Undirected graph

    Returns
    -------
    min_edge_dominating_set : set
      Returns a set of dominating edges whose size is no more than 2 * OPT.

    Notes
    -----
    The algorithm computes an approximate solution to the edge dominating set
    problem. The result is no more than 2 * OPT in terms of size of the set.
    Runtime of the algorithm is $O(|E|)$.
    """
    if not G:
        raise ValueError("Expected non-empty NetworkX graph!")
    return maximal_matching(G)
