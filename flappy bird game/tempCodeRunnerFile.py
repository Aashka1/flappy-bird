        for i in range(2):
            if Pipes_up[i]['x'] < bird_x < Pipes_up[i]['x'] + pipe_img1.get_width():
                score += 1
                score_text = font.render(f"Score: {score}", True, (0, 0, 0))