% Considerando que:
% Nota de 7.0 á 10.0 = Aprovado.
% Nota de 5.0 á 6.9 = Recuperação.
% Nota de 0.0 á 4.9 = Reprovado.

% FATOS
nota(joao, 5.0).
nota(maria, 6.0).
nota(joana, 8.0).
nota(mariana, 9.0).
nota(cleuza, 8.5).
nota(jose, 6.5).
nota(joaquim, 4.5).
nota(mara, 4.0).
nota(mary, 10.0).

% REGRAS
aprovado(X) :-
  nota(X, Y),
  Y > 6.9.


recuperacao(X) :-
  nota(X, Y),
  Y > 4.9,
  Y < 7.


reprovado(X) :-
  nota(X, Y),
  Y >= 0,
  Y < 5.
