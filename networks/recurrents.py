import torch.nn as nn


class BeliefUnit(nn.Module):
    """
    f_θ1 : R^2n * R^3n -> R^2n
    """
    def __init__(self, n: int) -> None:
        super().__init__()

        self.__n = n

        self.lstm = nn.LSTMCell(self.__n * 3, self.__n)

    def forward(self, h_t, c_t, u_t):
        # h_t.size() == (1, nb_agent, batch_size, hidden)
        #assert u_t.size(1) == 1, "Only one time iteration is allowed"

        #h_t, c_t = h_t[:u_t.size(0), :], c_t[:u_t.size(0), :]

        nb_ag, batch_size, hidden_size = h_t.size()

        h_t, c_t, u_t = h_t.flatten(0, 1), c_t.flatten(0, 1), u_t.flatten(0, 1)

        h_t_next, c_t_next = self.lstm(u_t, (h_t, c_t))

        return h_t_next.view(nb_ag, batch_size, -1), c_t_next.view(nb_ag, batch_size, -1)


class ActionUnit(nn.Module):
    """
    f_θ2 : ?
    Supposition : R^2n * R^3n -> R^2n
    R^2n : pas sûr
    """
    def __init__(self, n: int) -> None:
        super().__init__()

        self.__n = n

        # TODO find hidden state size in article
        self.lstm = nn.LSTMCell(self.__n * 3, self.__n)

    def forward(self, h_caret_t, c_caret_t, u_t):
        #assert u_t.size(1) == 1, "Only one time iteration is allowed"

        #h_caret_t, c_caret_t = h_caret_t[:u_t.size(0), :], c_caret_t[:u_t.size(0), :]

        nb_ag, batch_size, hidden_size = h_caret_t.size()

        h_caret_t, c_caret_t, u_t = h_caret_t.flatten(0, 1), c_caret_t.flatten(0, 1), u_t.flatten(0, 1)

        h_caret_t_next, c_caret_t_next = self.lstm(u_t, (h_caret_t, c_caret_t))

        return h_caret_t_next.view(nb_ag, batch_size, -1), c_caret_t_next.view(nb_ag, batch_size, -1)
