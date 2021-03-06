from unittest import TestCase
import numpy as np
from athena.subspaces import Subspaces


class TestUtils(TestCase):
    def test_init_W1(self):
        ss = Subspaces()
        self.assertIsNone(ss.W1)

    def test_init_W2(self):
        ss = Subspaces()
        self.assertIsNone(ss.W2)

    def test_init_evals(self):
        ss = Subspaces()
        self.assertIsNone(ss.evals)

    def test_init_evects(self):
        ss = Subspaces()
        self.assertIsNone(ss.evects)

    def test_init_evals_br(self):
        ss = Subspaces()
        self.assertIsNone(ss.evals_br)

    def test_init_subs_br(self):
        ss = Subspaces()
        self.assertIsNone(ss.subs_br)

    def test_init_dim(self):
        ss = Subspaces()
        self.assertIsNone(ss.dim)

    def test_init_cov_matrix(self):
        ss = Subspaces()
        self.assertIsNone(ss.cov_matrix)

    def test_compute(self):
        ss = Subspaces()
        with self.assertRaises(NotImplementedError):
            ss.compute()

    def test_forward(self):
        ss = Subspaces()
        with self.assertRaises(NotImplementedError):
            ss.forward(42)

    def test_backward(self):
        ss = Subspaces()
        with self.assertRaises(NotImplementedError):
            ss.backward(10, 10)

    def test_partition_01(self):
        np.random.seed(42)
        matrix = np.random.uniform(-1, 1, 9).reshape(3, 3)
        ss = Subspaces()
        ss.evects = matrix
        ss.partition(dim=2)
        np.testing.assert_array_almost_equal(matrix[:, :2], ss.W1)

    def test_partition_02(self):
        np.random.seed(42)
        matrix = np.random.uniform(-1, 1, 9).reshape(3, 3)
        ss = Subspaces()
        ss.evects = matrix
        ss.partition(dim=2)
        np.testing.assert_array_almost_equal(matrix[:, 2:], ss.W2)

    def test_partition_03(self):
        np.random.seed(42)
        matrix = np.random.uniform(-1, 1, 9).reshape(3, 3)
        ss = Subspaces()
        ss.evects = matrix
        with self.assertRaises(TypeError):
            ss.partition(dim=2.0)

    def test_partition_04(self):
        np.random.seed(42)
        matrix = np.random.uniform(-1, 1, 9).reshape(3, 3)
        ss = Subspaces()
        ss.evects = matrix
        with self.assertRaises(ValueError):
            ss.partition(dim=0)

    def test_partition_05(self):
        np.random.seed(42)
        matrix = np.random.uniform(-1, 1, 9).reshape(3, 3)
        ss = Subspaces()
        ss.evects = matrix
        with self.assertRaises(ValueError):
            ss.partition(dim=4)

    def test_bootstrap_replicate_01(self):
        np.random.seed(42)
        matrix = np.random.uniform(-1, 1, 9).reshape(3, 3)
        weights = np.ones((3, 1)) / 3
        ss = Subspaces()
        wei = ss._bootstrap_replicate(matrix, weights)[1]
        np.testing.assert_array_almost_equal(weights, wei)

    def test_bootstrap_replicate_02(self):
        np.random.seed(42)
        matrix = np.random.uniform(-1, 1, 9).reshape(3, 3)
        weights = np.ones((3, 1)) / 3
        ss = Subspaces()
        mat = ss._bootstrap_replicate(matrix, weights)[0]
        true_matrix = np.array([[-0.88383278, 0.73235229, 0.20223002],
                                [0.19731697, -0.68796272, -0.68801096],
                                [-0.25091976, 0.90142861, 0.46398788]])
        np.testing.assert_array_almost_equal(true_matrix, mat)

    def test_plot_eigenvalues(self):
        ss = Subspaces()
        with self.assertRaises(ValueError):
            ss.plot_eigenvalues(figsize=(7, 7), title='Eigenvalues')

    def test_plot_eigenvectors(self):
        ss = Subspaces()
        with self.assertRaises(ValueError):
            ss.plot_eigenvectors(n_evects=2, title='Eigenvectors')

    def test_plot_sufficient_summary(self):
        ss = Subspaces()
        inputs = np.diag(np.ones(3))
        outputs = np.ones(3).reshape(3, 1)
        with self.assertRaises(ValueError):
            ss.plot_sufficient_summary(inputs,
                                       outputs,
                                       figsize=(7, 7),
                                       title='Sufficient_summary_plots')
