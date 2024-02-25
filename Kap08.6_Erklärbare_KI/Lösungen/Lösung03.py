# Lösungsbeispiel
idx = 63  # andere Datenpunkte: 133, 83, 78, 63
np.random.seed(4)
exp = explainer.explain_instance(
    data_row     = X_test.loc[idx], 
    predict_fn   = model.predict_proba,
    num_features = 4,
    top_labels   = 3
)
exp.show_in_notebook(show_table=True);
print("Die vorhergesagte Schwertlilienart ist: ", model.predict(X_test.loc[[idx]])[0])
print("Die tatsächliche  Schwertlilienart ist: ", y_test.loc[idx][0])
fig = exp.as_pyplot_figure(1)
fig = exp.as_pyplot_figure(2)