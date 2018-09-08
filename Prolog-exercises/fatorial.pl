fatorial(0,1).

fatorial(X,R) :-
  X>0,
  N is X-1,
  fatorial(N, RA),
  R is RA * X.
  