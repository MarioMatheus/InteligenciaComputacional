% Seja o casal José e Maria e seus dois filhos, o João e a Ana.
% Ana teve duas filhas, a Helena e a Joana.
% Mário é filho do João.
% Carlos nasceu da relação entre a Helena e o Mário.

% FATOS
progenitor(jose, joao).
progenitor(jose, ana).

progenitor(maria, joao).
progenitor(maria, ana).

progenitor(ana, helena).
progenitor(ana, joana).

progenitor(joao, mario).

progenitor(helena, carlos).
progenitor(mario, carlos).

masculino(jose).
masculino(joao).
masculino(mario).
masculino(carlos).

feminino(ana).
feminino(maria).
feminino(helena).
feminino(joana).


% REGRAS
pai(X, Y) :-
  masculino(X),
  progenitor(X, Y).

mae(X, Y) :-
  feminino(X),
  progenitor(X, Y).

irmao(X, Y) :-
  masculino(X),
  progenitor(P, X),
  progenitor(P, Y).

irma(X, Y) :-
  feminino(X),
  progenitor(P, X),
  progenitor(P, Y).

% descendente(X,Y) :-
%   progenitor(X,Y).
 
% descendente(X,Y) :-
%   progenitor(X,Z),
%   descendente(Z,Y).

avo(X, Y) :-
  pai(P, Y),
  pai(X, P).

% tio(X, Y) :-
%   progenitor(P, Y),
%   irmao(I, P),
%   I == X.

% primo(X, Y) :-
%   pai(P, Y),
%   pai(P2, X),
%   irmao(P, P2).
