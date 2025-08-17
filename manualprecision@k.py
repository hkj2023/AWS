def precision_at_k(model, user_id, k=5):
    recommended = model.recommend(user_id, k)
    relevant = test[test['user_idx'] == user_id]['item_idx'].tolist()
    hits = len(set([i for i, _ in recommended]) & set(relevant))
    return hits / k